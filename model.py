from llama_cpp import Llama
import os

n_threads = os.cpu_count()
GPU_LAYERS = 40

llm = Llama(
    model_path="tinyllama-1.1b-chat-v1.0.Q8_0.gguf",
    n_ctx=4096,
    n_threads=n_threads,
    batch_size=4096,
    n_gpu_layers=GPU_LAYERS
)

def generate_answer_fast(question, context, max_context_length=500):
    context = " ".join(context.split()[:max_context_length])

    prompt = f"""You are an AI assistant specializing in Vietnam's traffic laws.  
Your responses must be:  
✅ **Accurate and legally sound**  
✅ **Based strictly on the provided legal information**  
✅ **Including relevant legal citations when applicable**  
✅ **Avoiding speculation or invented details**  

### **Relevant Law Information:**  
---  
{context}  
---  

### **Answering Guidelines:**  
1. Provide a **detailed and comprehensive response** based on the law.  
2. Cite **specific legal articles, decrees, and penalties** when relevant.  
3. If the question is unclear or lacks context, respond with:  
   _"I need more legal details to provide an accurate answer."_  
4. **Do not assume or make up any legal provisions.**  

Now, answer the following question thoroughly:  

**Q: {question}**  

**A:**  
"""


    response = llm(
        prompt, 
        max_tokens=80,  
        stop=["Q:"],  
        temperature=0.1,  # Giảm để tránh câu trả lời lộn xộn
        top_p=0.7,  
        top_k=20  
    )
    
    return response["choices"][0]["text"].strip()
