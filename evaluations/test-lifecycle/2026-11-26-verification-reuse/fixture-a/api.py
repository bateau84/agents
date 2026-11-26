import json
import sys
from domain import qualifies

def response(amount: int, minimum: int) -> str:
    return json.dumps({"eligible": qualifies(amount, minimum), "minimum": minimum}) + "\n"

if __name__ == "__main__":
    request = json.load(sys.stdin)
    sys.stdout.write(response(request["amount"], request["minimum"]))
