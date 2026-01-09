# ASCII Camera
Convert camera image to ASCII graphic

## Why This Repository Exists?

Ever wondered how AI can learn to generate ASCII graphics?  
Before jumping into AI, it helps to understand how ASCII art works in the first place.

ASCII graphics rely on a few simple ideas:

- **Character density** (for example, `@` appears darker than `.`)
- **Monospace fonts**
- **Fixed-width grids**, where each character acts like a pixel

From there, things get interesting. AI does not “see” ASCII art the way humans do. Instead, it learns **patterns** from large numbers of examples—how characters form lines, how shading emerges from frequency, and how perspective can be implied using symbols.

This repository starts at the foundation: a **simple, algorithmic ASCII generator**. It shows how images and camera frames can be converted into ASCII *without AI*, making the underlying mechanics explicit.

## Where AI Comes In

Conceptually, an AI-based approach builds on this foundation:

- **Dataset**: thousands of ASCII images  
- **Model**: transformer or diffusion-style text model  
- **Input**: prompt or rough sketch  
- **Output**: structured ASCII layouts  

Through training, the model learns:

- Line continuity  
- Shading via character distribution  
- Perspective and structural tricks  

This project focuses on understanding the fundamentals first—because good AI starts with good representations.






