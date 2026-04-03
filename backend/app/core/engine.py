@router.post("/run")
def run(payload: dict):
    return run_engine(payload)


def run_engine(input_data):
    return {
        "status": "success",
        "input": input_data,
        "message": "Trileon is running"
    }


