const commentInput = document.getElementById("commentInput");
const commentList = document.getElementById("commentList");

// Cargar comentarios desde localStorage
window.onload = () => {
    const saved = JSON.parse(localStorage.getItem("comments")) || [];
    saved.forEach(comment => renderComment(comment));
};

function addComment() {
    const text = commentInput.value.trim();
    if (text === "") return;

    const comment = {
        text,
        timestamp: new Date().toISOString()
    };

    saveComment(comment);
    renderComment(comment);
    commentInput.value = "";
}

function renderComment({
    text,
    timestamp
}) {
    // Quitar mensaje de "sin comentarios"
    const emptyMsg = document.querySelector(".no-comments");
    if (emptyMsg) emptyMsg.remove();

    const commentDiv = document.createElement("div");
    commentDiv.className = "comment";

    const time = new Date(timestamp).toLocaleString("es-MX");

    commentDiv.innerHTML = `
        <time>${time}</time>
        <p>${text}</p>
      `;

    commentList.appendChild(commentDiv);
}

function saveComment(comment) {
    const comments = JSON.parse(localStorage.getItem("comments")) || [];
    comments.push(comment);
    localStorage.setItem("comments", JSON.stringify(comments));
}