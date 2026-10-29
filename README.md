# Science Motion Video — V3.0

Minimalist science explainer rendered with **Remotion** (1920x1080, 30fps, 60s). Optional **Manim** mathematical animation under `/manim`.

## 1. Requirements
- Node.js 20+ and npm
- Chrome/Chromium and FFmpeg available (Remotion can provision its renderer binaries)
- Optional Python 3.11+ and Manim system requirements for Manim renders

## 2. Preview / render
```bash
npm install
npm run dev
npm run render
```
Open Remotion Studio; select `ProbabilityV3`. Output: `out/probability-v3.mp4`. This project does **not** require Supabase or Cloudflare.

## 3. Vietnamese narration
Record or generate a single 60s narration file `public/audio/narration.mp3`. Uncomment the `<Audio>` JSX tag at the bottom of `src/video.tsx`. For scene-perfect timing, create 6 audio chunks and place them using `<Sequence from={i*300}>` (30fps) and `<Audio>` elements. Keep licenses and rights to generated voice/music. **No narration or sound effects are bundled by default.**

## 4. Manim optional render
```bash
python -m venv .venv
# activate .venv
pip install -r manim/requirements.txt
manim -qh manim/probability.py CoinConvergence
```
Manim produces a separate clip for manual compositing; it is **not** automatically integrated into the Remotion timeline yet. The main Remotion video includes its own deterministic line graph and works independently.

## 5. GitHub deployment
Create a **private** repository `science-motion-video`, upload the contents of this folder (not the enclosing zip). Or from a local terminal:
```bash
git init
git add .
git commit -m "feat: probability V3 remotion project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/science-motion-video.git
git push -u origin main
```
Do not push voice service API keys. Render locally; do not host the compute on Cloudflare Workers Free.

## Status
Source implementation complete; actual npm compilation and 1080p render depend on a local npm install and browser runtime. No claim that the V3 MP4 is already rendered.
