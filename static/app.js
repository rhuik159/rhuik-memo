function editMemo(event) {
  console.log(event.target.data.id);
}

function displayMemo(memo) {
  const ul = document.querySelector("#memo-ul");
  const li = document.createElement("li");

  const editBtn = document.createElement("button");
  li.innerText = `[id:${memo.id}]${memo.content}`;

  editBtn.innerText = "수정하기";
  editBtn.addEventListener("click", editMemo);
  editBtn.dataset.id = memo.id;

  ul.appendChild(li);
  li.appendChild(editBtn);
}

async function readMemo() {
  const res = await fetch("/memos");
  const jsonRes = await res.json();
  const ul = document.querySelector("#memo-ul");
  ul.innerText = "";
  jsonRes.forEach(displayMemo);
}

async function createMemo(value) {
  const res = await fetch("/memos", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id: new Date().getTime(), content: value }),
  });
  readMemo();
}

function handleSubmit(event) {
  event.preventDefault();
  const input = document.querySelector("#memo-input");
  createMemo(input.value);
  input.value = "";
}
const form = document.querySelector("#memo-form");
form.addEventListener("submit", handleSubmit);

readMemo();
