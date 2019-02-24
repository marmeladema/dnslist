import appdirs
import argparse
import chevron
import dnslist
import logging
import os
import toml
import sys

appname = 'dnslist'

log_levels = [
    'CRITICAL',
    'DEBUG',
    'ERROR',
    'FATAL',
    'INFO',
    'WARN',
    'WARNING',
]

config_path = os.path.join(appdirs.user_config_dir(appname), 'config.toml')

parser = argparse.ArgumentParser(
    description = 'Generates a domain list from multiple sources.'
)
parser.add_argument(
    '-c',
    '--config',
    type = argparse.FileType('r'),
    default = config_path,
    help = 'Configuration file (default: {}).'.format(config_path)
)
parser.add_argument('-t', '--template', type = argparse.FileType('r'))
parser.add_argument('output', type = argparse.FileType('w'))
parser.add_argument('--log-level', choices = log_levels, default = 'INFO')


def main(cmdline = None):
	args = parser.parse_args(cmdline or sys.argv[1:])
	config = toml.load(args.config)
	logger = logging.getLogger(appname)
	logger.setLevel(getattr(logging, args.log_level.upper()))
	handler = logging.StreamHandler()
	formatter = logging.Formatter(
	    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
	)
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	template = args.template.read() if args.template else '{{ domain }}\n'
	domains = dnslist.DomainSet()

	for name, source in config.get('source', {}).items():
		logger.info('{}: loading source ...\r'.format(name))
		url = source.pop('url')
		n = domains.load(url, **source, logger = logger)
		logger.info('{}: {} domains loaded\r'.format(name, n))
	logger.info('Total: {} unique domains loaded\r'.format(len(domains)))
	for domain in sorted(domains):
		args.output.write(chevron.render(template, {'domain': domain}))


if __name__ == "__main__":
	main()
