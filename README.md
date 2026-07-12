# Dayton Technical Services Website

A framework-free static website for a Dayton, Ohio technical-services provider. It uses plain HTML, CSS, and JavaScript and is configured for deployment on Vercel.

## Project structure

- `index.html` — Home
- `services.html` — Services
- `products.html` — Digital Products
- `about.html` — About
- `contact.html` — Contact / Request a Quote
- `styles.css` — Shared responsive styles
- `script.js` — Mobile navigation and quote-form behavior
- `favicon.svg`, `robots.txt`, `sitemap.xml` — deployment and discovery assets
- `vercel.json` — Vercel clean URLs and security headers

## Required configuration before launch

Replace these explicit placeholders throughout the project:

- `Lapointa IT Services`
- `[Business email]`
- `[Business phone]`
- `REPLACE-WITH-BUSINESS-EMAIL` in `script.js`
- `YOUR-VERCEL-DOMAIN` in `sitemap.xml`

After the production URL is known, add its sitemap URL to `robots.txt`, for example:

```text
Sitemap: https://your-domain.example/sitemap.xml
```

## Run locally

No packages are required. From the project directory, start any static file server:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

## Production build

This is a static site, so there is no compilation or production build command. The checked-in files are the production artifact. Validate the site locally with:

```bash
python3 scripts/validate.py
```

On Vercel, leave **Build Command** and **Output Directory** empty. The framework preset should be **Other**.

## Deploy to Vercel

### Git integration

1. Create a Git repository, commit the files, and push it to GitHub, GitLab, or Bitbucket.
2. In Vercel, choose **Add New → Project** and import the repository.
3. Set **Framework Preset** to **Other**.
4. Leave **Build Command** and **Output Directory** blank.
5. Deploy.
6. Replace `YOUR-VERCEL-DOMAIN` in `sitemap.xml` with the assigned domain, add the sitemap line to `robots.txt`, commit, and push again.

### Vercel CLI

After installing and authenticating the Vercel CLI:

```bash
vercel
vercel --prod
```

The first command links the local directory and creates a preview deployment. The second creates the production deployment.

## Contact form behavior

The quote form prepares a pre-addressed email in the visitor's email application. A real, verified recipient must replace `REPLACE-WITH-BUSINESS-EMAIL` in `script.js` before launch. Until then, the contact route is intentionally not represented as production-ready.
