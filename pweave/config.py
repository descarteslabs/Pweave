import re

rcParams = {
    "cachedir": "cache",
    "figdir": "figures",
    "storeresults": False,
    "usematplotlib": True,
    "chunk": {
        "defaultoptions": {
            "allow_exceptions": False,
            "caption": False,
            "chunk_type": "code",
            "complete": True,
            "display_data": True,
            "display_stream": True,
            "dpi": 200,
            "echo": True,
            "evaluate": True,
            "f_env": None,
            "f_pos": "htpb",
            "f_size": (6, 4),
            "f_spines": True,
            "fig": True,
            "include": True,
            "multi_fig": True,
            "name": None,
            "option_string": "",
            "results": "verbatim",
            "term_prompts": False,
            "term": False,
            "wrap": "output",
        }
    },
}


class PwebProcessorGlobals(object):
    """A class to hold the globals used in processors"""

    globals = {}


class PwebError(Exception):
    ansi_escape = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")

    def __init__(self, exceptions=None):
        self.exceptions = ["Found exceptions while evaluating code blocks:"]
        self.exceptions.extend(exceptions or ["Strange, no exceptions found?"])

        super().__init__(
            "\n".join([self.ansi_escape.sub("", exc) for exc in self.exceptions])
        )
