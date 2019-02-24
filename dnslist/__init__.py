import io
import logging
import re
import requests
from requests_file import FileAdapter
import validators


class DomainSet(set):
	def __init__(self, *args, **kwargs):
		super(*args, **kwargs)
		self.logger = logging.getLogger(type(self).__name__)
		self.logger.addHandler(logging.NullHandler())

	def load(self, url, filter = None, group = 1, timeout = 60, logger = None):
		if not logger:
			logger = self.logger

		logger.debug('Retrieving domain list at {}'.format(url))
		s = requests.Session()
		s.mount('file://', FileAdapter())
		response = s.get(url, timeout = timeout)
		regexp = re.compile(filter) if filter else None
		ok, ko = 0, 0
		for line in io.StringIO(response.text).readlines():
			if regexp:
				match = regexp.search(line)
				line = match.group(group) if match else None
			domain = line.strip() if line else ''
			if domain and not any(map(line.startswith, ['#', '//'])):
				logger.debug('Adding domain {}'.format(domain))
				try:
					self.add(domain)
					ok += 1
				except ValueError as e:
					logger.error(str(e))
					ko += 1
		return (ok, ko)

	def add(self, domain):
		valid = validators.domain(domain)
		if valid is not True:
			raise ValueError('{} is not a valid domain name'.format(domain))
		super().add(domain)
