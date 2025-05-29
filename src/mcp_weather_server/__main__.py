from argparse import ArgumentParser

from . import main

if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--transport", choices=["stdio", "sse", "streamable-http"], default="stdio")
    args = arg_parser.parse_args()

    main(transport=args.transport)
