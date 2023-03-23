# crohme_visualize
Visualized web for model evaluation and data observation [CROHME](https://crohme2023.ltu-ai.dev)

---
**The web contains 4 windows:**
- Window for input image.
- Window for expected LaTeX predictions.
- Window for output LaTeX mathematic expression predictions.
- Window for converted LaTeX predictions.  

**Build with Docker:**

You can custom port in Dockerfile.

```docker build -t image_name. ```

**Run:**

```docker run --name container_name -v /dir:/dir -p 9000:9000 image_name```
