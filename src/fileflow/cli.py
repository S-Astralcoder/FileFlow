import argparse

class CLI:
    def __init__(self) -> None:
        self.arg_parser = argparse.ArgumentParser()
        self.operation_parser = self.arg_parser.add_subparsers(dest="operation", description="operation to be performed", required=True)


        self._add_global_options()
        self._add_create_option()
        self._add_copy_option()
        self._add_move_option()
        self._add_delete_option()
        self._add_workspace_global_delete_option()
        self._add_extract_option()
        self._add_script_option()

    def _add_global_options(self):
        self.arg_parser.add_argument("-ws", "--workspace", help="directory path to the workspace", default=".", type=str)
        
        self.arg_parser.add_argument("-f", "--force", action="store_true", help="allows actions that are dangerous")

    def _add_create_option(self):
        create_parser = self.operation_parser.add_parser("create", help="operation used to create file/directory")
        type = create_parser.add_mutually_exclusive_group(required=True)
        type.add_argument("-f", "--file", action="store_true")
        type.add_argument("-d", "--directory", action="store_true")
        create_parser.add_argument("-r", "--recursive", action="store_true" , help="creates parent folder if not exists")
        create_parser.add_argument("item", help="name of file or directory to be created", type=str)

    def _add_copy_option(self):
        copy_parser = self.operation_parser.add_parser("copy", help="operation to copy file/directory to a give destination")
        type = copy_parser.add_mutually_exclusive_group(required=True)
        type.add_argument("-f", "--file", action="store_true")
        type.add_argument("-d", "--directory", action="store_true")
        copy_parser.add_argument("-sf", "--soft-force", action="store_true" ,help="used to perform dangerous operation safely")
        copy_parser.add_argument("source", help="item path to be copied")
        copy_parser.add_argument("destination", help="path for the item to be copied to")

    def _add_move_option(self):
        move_parser = self.operation_parser.add_parser("move", help="operation to move file/directory to a give destination")
        type = move_parser.add_mutually_exclusive_group(required=True)
        type.add_argument("-f", "--file", action="store_true")
        type.add_argument("-d", "--directory", action="store_true")
        move_parser.add_argument("-sf", "--soft-force", action="store_true" ,help="used to perform dangerous operation safely")
        move_parser.add_argument("source", help="item path to be moved")
        move_parser.add_argument("destination", help="path for the item to be moved to")

    def _add_delete_option(self):
        delete_parser = self.operation_parser.add_parser("delete", help="operation to delete file/directory")
        type = delete_parser.add_mutually_exclusive_group(required=True)
        type.add_argument("-f", "--file", action="store_true")
        type.add_argument("-d", "--directory", action="store_true")
        delete_parser.add_argument("item", help="path of item to be deleted")

    def _add_workspace_global_delete_option(self):
        global_delete_parser = self.operation_parser.add_parser("gdelete", help="operation to perform a patten based deleted inside a given directory")
        type = global_delete_parser.add_mutually_exclusive_group(required=True)
        type.add_argument("-f", "--file", action="store_true")
        type.add_argument("-d", "--directory", action="store_true")
        global_delete_parser.add_argument("source", help="directory path to look under for match")
        global_delete_parser.add_argument("pattern", help="pattern for specify items to be deleted")

    def _add_extract_option(self):
        pack_items_parser = self.operation_parser.add_parser("extract", help="operation to find all the files under a directory and extract it into a given directory")
        pack_items_parser.add_argument("source", help="directory path to look under for match")
        pack_items_parser.add_argument("pattern", help="pattern for specify items to be extracted")
        pack_items_parser.add_argument("destination", help="directory to store the extracted items")

    def _add_script_option(self):
        script_parser = self.operation_parser.add_parser("script", help="execute operation script")
        script_parser.add_argument("source", help="path to the script file")
        script_parser.add_argument("-d", "--dry-run", help="user to perform only a demo run of the script")

    def _add_undo_option(self):
        undo_parser = self.operation_parser.add_parser("undo", help="used to undo operation performed")

    def start_cli(self, args : list[str] | None = None):
        arg = self.arg_parser.parse_args(args=args)
        