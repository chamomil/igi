from cli_storage import CliStorage


if __name__ == '__main__':
    storage = CliStorage()
    while True:
        try:
            storage.run()
        except Exception:
            continue
        break
