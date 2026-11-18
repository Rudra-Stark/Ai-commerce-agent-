const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const sendButton = document.getElementById("send-button");
const productList = document.getElementById("product-list");

function addMessage(message, sender) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", sender);
    messageElement.textContent = message;

    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;

    return messageElement;
}

// Send message to FastAPI AI agent
chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = userInput.value.trim();

    if (!message) return;

    addMessage(message, "user");
    userInput.value = "";

    sendButton.disabled = true;
    sendButton.textContent = "...";

    const loadingMessage = addMessage("Thinking...", "assistant");

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error("Server returned an error: " + response.status);
        }

        const data = await response.json();

        loadingMessage.textContent = data.response || "I couldn't generate a response.";

    } catch (error) {
        loadingMessage.textContent =
            "Unable to connect to the AI server. Please check whether FastAPI is running.";

        console.error(error);

    } finally {
        sendButton.disabled = false;
        sendButton.textContent = "Send ↗";
        userInput.focus();
    }
});

// Suggested prompts
document.querySelectorAll(".suggestion").forEach((button) => {
    button.addEventListener("click", () => {
        userInput.value = button.textContent;
        userInput.focus();
    });
});

// Load products from FastAPI
async function loadProducts() {
    productList.textContent = "Loading products...";

    try {
        const response = await fetch("/products");

        if (!response.ok) {
            throw new Error("Unable to load products");
        }

        const products = await response.json();

        productList.replaceChildren();

        if (products.length === 0) {
            productList.textContent = "No products available.";
            return;
        }

        products.forEach((product) => {
            const card = document.createElement("article");
            card.className = "product-card";

            const category = document.createElement("p");
            category.className = "product-category";
            category.textContent = product.category;

            const name = document.createElement("h3");
            name.textContent = product.name;

            const description = document.createElement("p");
            description.className = "product-description";
            description.textContent = product.description || "No description available.";

            const bottom = document.createElement("div");
            bottom.className = "product-bottom";

            const price = document.createElement("span");
            price.className = "product-price";
            price.textContent = "₹" + Number(product.price).toLocaleString("en-IN");

            const rating = document.createElement("span");
            rating.className = "product-rating";
            rating.textContent = product.rating
                ? "★ " + product.rating
                : "No rating";

            bottom.append(price, rating);
            card.append(category, name, description, bottom);
            productList.appendChild(card);
        });

    } catch (error) {
        productList.textContent = "Could not load products. Check the backend.";
        console.error(error);
    }
}

document.getElementById("refresh-products")
    .addEventListener("click", loadProducts);

loadProducts();