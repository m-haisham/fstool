from pathlib import Path
import shutil


def restructure(config: dict, home: str, files: list = [], verbose: bool = False, move: bool = True):
    home = Path(home)

    # create Path objects from all files
    files = [Path(i) for i in files]

    # file loop
    for file in files:

        new_file = None

        try:
            # if file specified
            match_object = config[file.parts[-1]]  # get the matching object from config

            # get Path of new file
            new_file = home / Path(match_object['dir']) / Path(
                f'{file.stem}{match_object["file"][1:]}' if match_object["file"][:2] == '*.' else match_object["file"])
        except KeyError:
            # or else if extension specified
            if f'*{file.suffix}' in config.keys():
                match_object = config[f'*{file.suffix}']  # get the matching object from config

                # get Path of new file
                new_file = home / Path(match_object['dir']) / Path(
                    f'{file.stem}{match_object["file"][1:]}' if match_object["file"][:2] == '*.' else match_object[
                        "file"])

        # if no new file skip
        if not new_file:
            continue

        # create parent directory
        new_file.parent.mkdir(parents=True, exist_ok=True)

        if verbose:
            print(f'[{"MOVE" if move else "COPY"}] {file} -> {new_file}')

        if not new_file.exists():
            # copy file to new location
            shutil.copy(str(file), str(new_file))
        if move:
            # remove old file
            file.unlink()
