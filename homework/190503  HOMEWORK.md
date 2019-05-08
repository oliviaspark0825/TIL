## 190503 | HOMEWORK

### 1. v-model 디렉티브는 input, textarea, select와 같은 엘리먼트들과 ____(a)____을 생성합니다. 빈칸 (a)에 들어 갈 말을 작성하시오.

```
양방향 데이터 바인딩
```



### 2. v-model 디렉티브는 엘리먼트의 종류에 따라 인스턴스의 속성을 업데이트하는 데이터의 타입이 다릅니다. 아래의 엘리먼트들이 기본적으로 어떠한 데이터 타입으로 인스턴스의 속성을 업데이트 하는지 https://kr.vuejs.org/v2/guide/forms.html를 참고하여 작성하시오

```
- input
	<input v-model="message" placeholder="여기를 수정해보세요">
	<p>메시지: {{ message }}</p>
	
- textarea
	<textarea v-model="message" placeholder="여러줄을 입력해보세요"></textarea>
	
- 단일 checkbox
	<input type="checkbox" id="checkbox" v-model="checked">
	<label for="checkbox">{{ checked }}</label>
	
- 다중 checkbox
	<div id='example-3'>
      <input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
      <label for="jack">Jack</label>
      <input type="checkbox" id="john" value="John" v-model="checkedNames">
      <label for="john">John</label>
      <input type="checkbox" id="mike" value="Mike" v-model="checkedNames">
      <label for="mike">Mike</label>
      <br>
      <span>체크한 이름: {{ checkedNames }}</span>
    </div>
    
- radio
	<input type="radio" id="one" value="One" v-model="picked">
    <label for="one">One</label>
    <br>
    <input type="radio" id="two" value="Two" v-model="picked">
    <label for="two">Two</label>
    <br>
    <span>선택: {{ picked }}</span>
    
- 단일 select
	<select v-model="selected">
      <option disabled value="">Please select one</option>
      <option>A</option>
      <option>B</option>
      <option>C</option>
    </select>
    <span>선택함: {{ selected }}</span>

- 다중 select
	<select v-model="selected" multiple>
      <option>A</option>
      <option>B</option>
      <option>C</option>
    </select>
    <br>
    <span>Selected: {{ selected }}</span>
```