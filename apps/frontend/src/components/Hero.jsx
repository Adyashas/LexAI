import { useState } from "react";

import ChatInput from "./ChatInput";
import ChatMessage from "./ChatMessage";

import { askLexAI } from "../services/api";

export default function Hero() {

  const [answer, setAnswer] = useState("");

  const [loading, setLoading] = useState(false);

  async function handleAsk(question) {

    setLoading(true);

    try {

      const result = await askLexAI(question);

      setAnswer(result.answer);

    } catch (err) {

      console.error(err);

      setAnswer("Something went wrong.");

    }

    setLoading(false);
  }

  return (
    <section className="mx-auto flex max-w-5xl flex-col items-center px-6 py-20 text-center">

      <h1 className="mb-6 text-6xl font-bold">
        AI Legal Rights
      </h1>

      <h2 className="mb-8 text-3xl font-semibold text-blue-700">
        & Guidance Assistant
      </h2>

      <ChatInput onAsk={handleAsk} />

      {loading && (
        <div className="mt-8 text-blue-700 text-lg">
          ⚖️ Thinking...
        </div>
      )}

      <ChatMessage answer={answer} />

    </section>
  );
}