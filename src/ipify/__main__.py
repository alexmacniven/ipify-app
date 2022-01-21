import argparse
import sys
import textwrap
import urllib.request
from typing import Sequence

import ipify


def get_ip() -> str:
    service_url: str = 'http://api.ipify.org'
    response = urllib.request.urlopen(service_url)
    return response.read().decode('utf-8')


def main_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=textwrap.indent(
            textwrap.dedent(
                '''
                Return your ip address, powered by api.ipify.org.
                '''
            ).strip(),
            '    ',
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        '--version',
        '-V',
        action='version',
        version=f'ipify {ipify.__version__}'
    )
    return parser


def main(cli_args: Sequence[str]) -> None:
    parser = main_parser()
    parser.parse_args(cli_args)
    print(get_ip())


def entrypoint() -> None:
    main(sys.argv[1:])


if __name__ == '__main__':
    main(sys.argv[1:])
