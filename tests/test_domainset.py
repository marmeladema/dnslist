import dnslist
import os
import random
import tempfile
import unittest

data_path = os.path.join(os.path.dirname(__file__), 'data')


class TestDomainSet(unittest.TestCase):
	def test_add_ok(self):
		domains = dnslist.DomainSet()
		self.assertEqual(len(domains), 0)
		domains.add('github.com')
		self.assertIn('github.com', domains)
		self.assertEqual(len(domains), 1)

	def test_add_ko(self):
		domains = dnslist.DomainSet()
		self.assertEqual(len(domains), 0)
		with self.assertRaises(ValueError):
			domains.add('github$com')

	def test_set(self):
		domains = dnslist.DomainSet()
		self.assertEqual(len(domains), 0)
		domains.add('github.com')
		self.assertEqual(len(domains), 1)
		domains.add('python.org')
		self.assertEqual(len(domains), 2)
		domains.add('github.com')
		self.assertEqual(len(domains), 2)
		domains.add('python.org')
		self.assertEqual(len(domains), 2)

	def test_load_simple(self):
		domains = dnslist.DomainSet()
		self.assertEqual(len(domains), 0)
		with tempfile.NamedTemporaryFile() as tmpfd:
			tmpfd.write(b'# A comment line\n')
			tmpfd.write(b'github.com\n')
			tmpfd.write(b'python.org\n')
			tmpfd.flush()
			domains.load('file://{}'.format(tmpfd.name))
			self.assertEqual(len(domains), 2)
			self.assertIn('github.com', domains)
			self.assertIn('python.org', domains)

	def test_load_filter(self):
		domains = dnslist.DomainSet()
		self.assertEqual(len(domains), 0)
		with tempfile.NamedTemporaryFile() as tmpfd:
			tmpfd.write(b'# A comment line\n')
			tmpfd.write(b'127.0.0.1 github.com\n')
			tmpfd.write(b'127.0.0.1 python.org\n')
			tmpfd.flush()
			domains.load(
			    'file://{}'.format(tmpfd.name),
			    filter = '^127.0.0.1 ([^\\s]+)'
			)
			self.assertEqual(len(domains), 2)
			self.assertIn('github.com', domains)
			self.assertIn('python.org', domains)
