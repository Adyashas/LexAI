import { useState } from "react";

export default function ChatInput({ onAsk }) {
  const [question, setQuestion] = useState("");

const handleSubmit = () => {
  if (!question.trim()) return;

  console.log("Button clicked");
  console.log(question);

  onAsk(question);

  setQuestion("");
};

  return (
    <div className="w-full max-w-3xl rounded-2xl bg-white p-6 shadow-lg">

      <textarea
        rows={3}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask your legal question..."
        className="w-full resize-none rounded-xl border p-4 outline-none focus:ring-2 focus:ring-blue-500"
      />

      <button
        onClick={handleSubmit}
        className="mt-5 w-full rounded-xl bg-blue-700 py-3 text-lg font-semibold text-white hover:bg-blue-800"
      >
        ⚖️ Ask LexAI
      </button>

    </div>
  );
}