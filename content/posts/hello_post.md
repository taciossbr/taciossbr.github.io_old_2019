title: Hello, World
date: 2018-12-30 13:40
tags: tag1, tag3
slug: teste
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


```python

import base64
import os
import sys
import json
from getpass import getpass
from urllib.request import urlopen, Request

url = "https://api.github.com/gists"

if len(sys.argv) < 3:
    print("USAGE:", sys.argv[0], "user", "file", "-p", "pass")
    sys.exit(1)

username = sys.argv[1]

if '-p' in sys.argv:
    password = sys.argv[sys.argv.index('-p')+1]
else:
    password = getpass()

filename = sys.argv[2]

if not os.path.exists(filename):
    print("arquivo inexistente", file=sys.stderr)
    sys.exit(1)

# passman.add_password(None, url, user, password)

base64string = base64.encodebytes(
    bytes(username+':'+password, 'utf-8')).replace(b'\n', b'')


auth = b"Basic " + base64string

headers = {
    'Authorization': auth,
    'content-type': 'application/json'
}

print(headers)


with open(filename, 'r') as file:
    s = ''.join(file.readlines())


    data = {
      "description": "Empty",
      "public": True,
      "files": {
        filename: {
          "content": s
        }
      }
    }

    data_json = json.dumps(data)
    data_bytes = data_json.encode('utf-8')

    req = Request(url, data=data_bytes, headers=headers)

    res = urlopen(req)

    data = json.loads(''.join(map(bytes.decode,res.readlines())))

    url = data['html_url']

    print(url)


```

```c
#include <stdio.h>

int main (void)
{
    int m, n;
    scanf(" %d %d", &m, &n);
    int i, l, mat[m][n], *p;
    for (i = 0, l = m *n, p = mat; i < l; i++)
    {
        scanf(" %d", p++);
    }
    int v[n], j, soma = 0, *p1 = v;
    for (i = 0, p = mat; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            soma += *p;
            p++;
        }
        *p1 = soma;
        p1++;
        soma = 0;
    }
    for (i = 0, p = v; i < n; i++)
    {
        printf("v[%d] = %d\n", i, *p);
        p++;
    }
    return 0;
}
```

