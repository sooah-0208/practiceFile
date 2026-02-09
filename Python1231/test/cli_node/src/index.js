console.log("여긴 자바스크립트")

import {Command} from "commander"
import {add, list} from "./cmd.js"

const program = new Command();

program
.command('add')  //content는 문자열임
.argument('<a>')
.argument('<b>')
.description('메모 추가')
.action(add);  //js는 add함수를 action함수 안에 콜백 해올 수 있음

program
.command('list')  
// .argument('<a>')
.description('목록보기')
.action(list); 

program.parse(process.argv)