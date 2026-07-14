# Personal academic website

A simple, single-page Jekyll site for GitHub Pages: research interests,
education, publications, and a link to the [PDF CV](assets/cv.pdf). Supports
light and dark themes (follows your OS preference, with a manual toggle).

## Run locally

Requires Ruby (3.x works) and Bundler.

```sh
bundle install
bundle exec jekyll serve
```

Then open <http://localhost:4000>.

## Deploy to GitHub Pages (user site)

1. Create a GitHub repository named exactly `<your-username>.github.io`.
2. Push this repo's `main` branch there:

   ```sh
   git remote add origin git@github.com:<your-username>/<your-username>.github.io.git
   git push -u origin main
   ```

3. On GitHub: **Settings → Pages → Build and deployment**, set Source to
   "Deploy from a branch", branch `main`, folder `/ (root)`.
4. The site goes live at `https://<your-username>.github.io/` within a minute
   or two.

## Things to fill in

- `_config.yml`: replace `github_username` and `linkedin_username`
  placeholders with your real handles.
- `index.md`: the "Beyond research" section has a placeholder hobbies list —
  make it yours.
- `assets/cv.pdf`: re-copy from `~/code/academic-cv/cv.pdf` whenever the CV
  changes.
