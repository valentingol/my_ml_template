"""Project configuration class."""

from yaecs import Configuration


class ProjectConfig(Configuration):
    """Project configuration class."""

    @staticmethod
    def get_default_config_path() -> str:
        """Return default config."""
        return "configs/default/main.yaml"

    def parameters_pre_processing(self) -> dict:
        """Pre-processing on some config parameters."""
        return {}

    def parameters_post_processing(self) -> dict:
        """Post-processing on some config parameters."""
        return {
            "experiment_path": self.register_as_experiment_path,
            "*_config_path": self.register_as_additional_config_file,
        }
