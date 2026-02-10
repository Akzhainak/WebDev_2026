const input = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const list = document.getElementById("list");

function addTask() {
  const text = input.value.trim();
  if (text === "") return;


  const li = document.createElement("li");
  li.className = "item";


  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";


  const span = document.createElement("span");
  span.className = "text";
  span.textContent = text;


  const delBtn = document.createElement("button");
  delBtn.className = "del-btn";
  delBtn.textContent = "DEL";


  checkbox.addEventListener("change", function () {
    span.classList.toggle("done");
  });


  delBtn.addEventListener("click", function () {
    li.remove();
  });

  li.appendChild(checkbox);
  li.appendChild(span);
  li.appendChild(delBtn);

  list.appendChild(li);

  input.value = "";
  input.focus();
}

addBtn.addEventListener("click", addTask);


input.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    addTask();
  }
});
