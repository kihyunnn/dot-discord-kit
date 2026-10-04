import { Glob } from "bun";
const root = process.cwd();
const forbidden = [
  /(?:gho|github_pat)_[A-Za-z0-9_]+/,
  /(?:Bot|Bearer)\s+[A-Za-z0-9._-]{20,}/,
  /\b(?:sk|xoxb|xoxp)-[A-Za-z0-9-]{12,}/,
  /\/home\/[A-Za-z0-9._-]+/,
  /\/mnt\/data[12]TB\//,
  /(?:155\d{15,}|8522984813)/,
  /(?:cookie|password|session[_-]?token)\s*[:=]\s*[^\s"']+/i
];
const files = [];
for await (const file of new Glob("**/*").scan({ cwd: root, onlyFiles: true, dot: true })) {
  if (file.startsWith(".git/") || file === "tools/privacy-scan.mjs") continue;
  files.push(file);
}
const hits = [];
let skippedBinary = 0;
for (const file of files) {
  const bytes = new Uint8Array(await Bun.file(`${root}/${file}`).arrayBuffer());
  if (bytes.includes(0)) { skippedBinary++; continue; }
  const text = new TextDecoder().decode(bytes);
  text.split("\n").forEach((line, index) => {
    if (forbidden.some((pattern) => pattern.test(line))) hits.push(`${file}:${index + 1}`);
  });
}
if (hits.length) {
  console.error(hits.join("\n"));
  console.error(`privacy-scan: ${files.length} files, ${hits.length} hit(s)`);
  process.exit(1);
}
console.log(`privacy-scan: ${files.length} files, ${skippedBinary} binary assets skipped, 0 hits`);
