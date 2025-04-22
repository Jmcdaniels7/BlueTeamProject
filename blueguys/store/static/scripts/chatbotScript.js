window.addEventListener("DOMContentLoaded", function () {
    const sendBtn = document.getElementById("send-btn");
    const input = document.getElementById("chat-input");
    const chatArea = document.getElementById("chat-area");

    let waitingForOrderConfirmation = false;

    function botMessage(string){
      setTimeout(() => {
        const botBubble = document.createElement("div");
        botBubble.className = "recieved-chats recieved-msg recieved-msg-inbox";
        botBubble.innerHTML = `<p>${string}</p>
        <span class="time" id="msg-time">${new Date().toLocaleTimeString([], { hour: '2-digit', minute:"2-digit"})}</span>`;
        chatArea.appendChild(botBubble);
        chatArea.scrollTop = chatArea.scrollHeight;
      }, 600);
    };

    async function loadUserData(){
      try {
        const response = await fetch("/static/fakeData/data.json");
        if (!response.ok) {
          throw new Error('Unable to connect to DB: ' + response.statusText);
        }
        const data = await response.json();
        console.log("fetched user data:", data);
        return data;
      } catch (error) {
        console.error('Error fetching user data', error);
        return null;
      }
    }

    async function handleUserMsg() {
      const message = input.value.trim();
      if (message === "") return;

      const userBubble = document.createElement("div");
      userBubble.className = "user-message user-message";
      userBubble.innerHTML = `
        <p>${message}</p>
        <span class="time" id="msg-time">${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
      `;
      chatArea.appendChild(userBubble);

      const lowerMsg = message.toLowerCase();
      
      if (waitingForOrderConfirmation) {
        if (lowerMsg.includes("yes")) {
          const jsonData = await loadUserData();
          console.log(jsonData);  
          if (jsonData && jsonData.data && jsonData.data.length) {
            const users = jsonData.data;
            const randUser = Math.floor(Math.random() * users.length);
            console.log("random number selected: " + randUser)
            const user = users[randUser];

            const reply = `Looks like your order (order number: ${user.order}) for ${user.description} at a total of ${user.price}.`;
            botMessage(reply);
          } else {
            botMessage("Couldn't load user data.");
            }
        } else if (lowerMsg.includes("no")) {
        botMessage("Okay, taking you back to the menu!");
        } else {
          botMessage("Sorry, I didn't understand. Could you enter 'Yes' or 'No'?");
        }
        waitingForOrderConfirmation = false;
      } else {
        if (lowerMsg.includes("order") || lowerMsg.includes("orders")) {
          botMessage("Would you like to see your order history?");
          waitingForOrderConfirmation = true;
        //  if (user)
        } else if (lowerMsg.includes("return")) {
          botMessage("Would you like to initiate a return?");
        } else if (lowerMsg.includes("help")) {
          botMessage("Type orders or returns to see more information about those items.");
        } else {
          botMessage("I don't understand. Please type 'orders' or 'returns' to see more info.");
        }
      }
      input.value = "";
      chatArea.scrollTop = chatArea.scrollHeight;
    }
    sendBtn.addEventListener("click", handleUserMsg);
    input.addEventListener("keydown", function (event){
      if (event.key === "Enter") {
        event.preventDefault();
        handleUserMsg();
      }
    });
  });
