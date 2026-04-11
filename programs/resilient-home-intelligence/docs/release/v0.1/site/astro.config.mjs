import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://resilient-home-intelligence.org",
  output: "static",
  build: {
    format: "file"
  },
  integrations: [mdx(), sitemap()],
  server: {
    host: true
  }
});
