import sys
import json

if __name__ == '__main__':
    x = [1, 'simple', 'list']
    json.dumps(x)
    with  open('/Users/xiangyusun/Downloads/2.csv', 'a', encoding='utf-8') as f:
        json.dump(x, f)
    with  open('/Users/xiangyusun/Downloads/2.csv', 'r', encoding='utf-8') as f:
        print(f.read())
