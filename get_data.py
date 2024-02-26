from datasets import load_dataset

def get_help_steer():
    ds = load_dataset("nvidia/HelpSteer")
    return ds
