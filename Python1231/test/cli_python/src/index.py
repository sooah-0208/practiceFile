print("여기는 파이썬")

import argparse
from cmd import add, list

parser = argparse.ArgumentParser(description="CLI 프로그램")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser('add', help="메모 추가")
add_parser.add_argument('a', help="1번째 값")
add_parser.add_argument('b', help="두번째 값")

add_parser = subparsers.add_parser('list', help="목록보기")

args = parser.parse_args()


if args.command == 'add':
    add(args.a, args.b) #파이썬은 콜백함수를 쓸 수 없어서 직접 함수 호출해야함
elif args.command == 'list':
    list()