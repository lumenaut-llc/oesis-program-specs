import { defineCollection, z } from "astro:content";

const publicPages = defineCollection({
  type: "content",
  schema: z.object({
    route: z.string(),
    title: z.string(),
    description: z.string(),
    eyebrow: z.string(),
    heroTitle: z.string(),
    intro: z.string(),
    navLabel: z.string(),
    navOrder: z.number(),
    public: z.boolean().default(true),
    section: z.string(),
    release: z.string().optional(),
    showDiagrams: z.boolean().default(false),
    readNext: z
      .array(
        z.object({
          href: z.string(),
          title: z.string(),
          body: z.string()
        })
      )
      .default([])
  })
});

export const collections = {
  publicPages
};
