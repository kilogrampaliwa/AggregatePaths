from aggregator import aggregator

class cleared:

    def __init__(self, lines: list[dict], configuration_address: str = "configuration.json"):

        configuration = self.__load_json(configuration_address)

        agg = aggregator.aggre(lines, configuration['banned'], configuration['wanted'], configuration['deleted'])

        self.lines = agg.lines
        self.one_line = agg.one_line


    def __load_json(self, address: str):

        output = {}
        with open(address, 'r') as file: output = file.readlines
        self.__check_configuration(output)

        if output["wanted"] == []: output["wanted"] = ['']
        if output["banned"] == []: output["banned"] = ['']
        if output["delete"] == []: output["delete"] = ['']

        return output


    def __check_configuration(self, config : dict):

        checklist = [False for key in ["wanted", "banned", "delete"] if key not in config.keys()]
        if False in checklist: raise ValueError
