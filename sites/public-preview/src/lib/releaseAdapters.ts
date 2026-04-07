import {
  legalRoot,
  privacyGovernanceRoot,
  programRoot,
  releaseRoot,
  repoBlobBase
} from "./paths";

export const repoLink = (path: string) => `${repoBlobBase}${programRoot}${path}`;
export const releaseDocPath = (path: string) => `${releaseRoot}${path}`;
export const privacyDocPath = (path: string) =>
  `${privacyGovernanceRoot}${path}`;
export const legalDocPath = (path: string) => `${legalRoot}${path}`;

export const releaseDocLink = (path: string) =>
  `${repoBlobBase}${releaseDocPath(path)}`;
export const privacyDocLink = (path: string) =>
  `${repoBlobBase}${privacyDocPath(path)}`;
export const legalDocLink = (path: string) =>
  `${repoBlobBase}${legalDocPath(path)}`;
