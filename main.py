"""Coinstack - Gamified Finance Habit Builder
Main entry point for the application.
"""

import argparse
from src.core.app import App
import sys

def main() -> None:
    """
    Parses command-line arguments and runs the Coinstack application.
    """
    parser = argparse.ArgumentParser(
        description="Coinstack: Gamified Finance Habit Builder for Gen Z.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0",
        help="Show program's version number and exit.\n        For example: python main.py --version"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode for more verbose output.\n        For example: python main.py --debug"
    )

    args = parser.parse_args()

    # Initialize and run the application
    debug_val = True if args.debug else None
    app = App(debug_mode=debug_val)
    app.run()

if __name__ == "__main__":
    main()
