def validate_environment_variables(required_vars):
    """Validates if all required environment variables are set."""
    missing_vars = [var for var in required_vars if not var]

    if missing_vars:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing_vars)}",
        )
