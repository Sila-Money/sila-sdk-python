from typing import Optional


class UrlParameters():
    @staticmethod
    def add_query_parameter(parameter_name: str, parameter_value: str, query_parameters: Optional[str] = None) -> str:
        """
        Args:
            parameter_name (str): The name of the parameter to add in the query parameters
            parameter_value (str): The value of the parameter to add in the query parameters
            query_parameters (str): The current query parameters text
                (default is None)
        Returns:
            str: The query parameters with the new parameter added at the end of the text
        """
        if query_parameters is None or len(query_parameters.strip()) == 0:
            query_parameters = '?'
        else:
            query_parameters += '&'
        query_parameters += '{parameter_name}={parameter_value}'.format(
            parameter_name=parameter_name, parameter_value=parameter_value)
        return query_parameters
