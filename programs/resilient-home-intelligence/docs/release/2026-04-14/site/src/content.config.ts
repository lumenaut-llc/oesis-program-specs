import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const docs = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/docs" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    section: z.enum([
      "getting-started",
      "data-model",
      "privacy",
      "hardware",
      "system",
      "build-guides",
      "pilot-playbooks",
      "legal"
    ]),
    audience: z
      .array(z.enum(["homeowner", "builder", "researcher", "contributor"]))
      .optional()
      .default([]),
    order: z.number().optional().default(100),
    draft: z.boolean().optional().default(false),
    schema_file: z.string().optional(),
    example_file: z.string().optional(),
    status: z.enum(["stable", "beta", "draft", "deprecated"]).optional()
  })
});

export const collections = { docs };
