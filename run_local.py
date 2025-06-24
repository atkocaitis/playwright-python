import pytest
import sys
import os

if __name__ == "__main__":
    extra_args = []

    if "--headed" in sys.argv:
        os.environ["HEADLESS"] = "false"
        sys.argv.remove("--headed")
        extra_args += ["--headed"]

    if "-n" in sys.argv:
        n_index = sys.argv.index("-n")
        try:
            workers = sys.argv[n_index + 1]
            extra_args += ["-n", workers]
        except IndexError:
            print("Missing value after -n")
            sys.exit(1)

    pytest_args = ["-v", "tests"] + extra_args
    raise SystemExit(pytest.main(pytest_args))