import re

s = input()
k = input()

matches = list(re.finditer(r"(?=%s)" % k, s))

if matches:
    for m in matches:
        print((m.start(), m.start() + len(k) - 1))
else:
    print((-1, -1))


curl -X GET 'http://v0-ic4v-sddc-flask.dev-test-automation.svc.cluster.local/private/v1/domain/e1c0f930-d2a1-4616-a576-3ece542e544a' -H 'Content-Type:application/json'
