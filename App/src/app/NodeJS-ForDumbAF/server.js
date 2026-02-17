const http = require('http');

const server = http.createServer((req, res) => {
  // Устанавливаем код ответа и заголовки
  res.writeHead(200, { 'Content-Type': 'application/json' });

  // Простая серверная логика (пример: расчёт победы)
  const win = Math.random() < 0.1; // 10% шанс победы

  const result = {
    outcome: win ? "🎉 WIN" : "💀 LOSE",
    reward: win ? 100 : 0,
  };

  // Отправляем результат как JSON
  res.end(JSON.stringify(result));
});

// Сервер слушает порт 3000
server.listen(3000, () => {
  console.log("Server is running on <http://localhost:3000>");
});