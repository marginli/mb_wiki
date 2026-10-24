# 日誌

只追加，新的在最上面。動作僅三種：`ingest` / `query` / `lint`（另有人類的 `裁決`）。

## [2026-10-25] lint | 主題頁、綜述頁、README 的冷讀與更正

- 冷讀 4 輪（每輪換新讀者）：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]、[[syn-contradictions]]、`README.md` 與 `index.md`。[[syn-contradictions]] 於第 3 輪起無「看不懂」。
- 冷讀抓到的內容錯誤：[[t-timing-rules]] 的逆向配對表把 PAM 的突觸結果與 PPL 的行為結果並排，方向推不通，已拆成兩列；同頁誤寫「兩篇都用光遺傳」，Handler 2019 的離體實驗用的是 P2X2＋ATP；「順向 cAMP 比逆向高 25–35%」驗算為 28–36%，全庫同步更正。
- 整合者回查發現並更正：[[s-tomchik-2009-camp-dynamics]] 的優先權宣稱（「第一批…之一」）與「末梢鈣越多、送出越多」的無出處說明；[[t-timing-rules]] 曾把 Hige 2015 的 PPL1 寫成 Handler 2019 的 PPL 的別名，改為「兩篇未說明是否同一群」。
- 三篇來源頁「未來」一節的「依題目推測另兩篇」改寫為實際對照。
- [[syn-contradictions]] 新增 4.4（兩篇的命名可能不同）。[[syn-changelog]] 更正清單增為 33 處。
- `README.md`：加入可點的全頁目錄、不用終端機的下載方式（ZIP＋Obsidian）、終端機與工具安裝說明。`tools/serve.sh` 移除母庫專用的連線提示。

## [2026-10-25] lint | 主題層、綜述、索引、登記簿

- 開兩條主題：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]。三篇都對兩條主題有實質且不同的說法。
- 開 7 個概念頁、8 個實體頁（皆至少兩篇實際使用）。三篇來源頁的「待開頁面」清單中，已開的改為連結，同義名稱併入同一頁（例：`c-temporal-contingency`、`c-trace-conditioning` 併入 [[c-cs-us-timing]]）。
- [[syn-contradictions]]：跨來源矛盾 2 條（1.1 逆向配對的效果；1.2 cAMP 能否分辨先後），單篇自身不一致索引 10 列，空缺 5 條，本庫不確定性 3 條。
- [[syn-changelog]]：階段一；更正清單 27 處（乙 5、丁 3、戊 6、庚 1、辛 2、壬 10）。
- 整合者抽查發現並更正：[[s-tomchik-2009-camp-dynamics]] 三處憑記憶補充的背景（KC 約兩千顆、「流傳二十年」、「2009 年才剛成熟」）；[[s-hige-2015-heterosynaptic-plasticity]] 一處內部用語；[[s-handler-2019-dopamine-receptor-timing]] 一處非客觀形容詞。
- `numbers.md` 併入三篇的數字節。`index.md`、`intake.md`（三篇改為已收錄，備註補充資料的人工下載網址）。
- 書目以 Crossref 核對三篇的卷期頁，與 citation 一致。

## [2026-10-25] ingest | Handler et al. 2019, Cell（DopR1／DopR2 與學習的時序敏感度）

新增 [[s-handler-2019-dopamine-receptor-timing]]，圖 7 張。冷讀 5 輪後無「看不懂」。單篇自身不一致 16 項，其中 DopR1 突變在順向配對後反而變強、模型解釋不了，是冷讀第二輪抓到的稽核點。補充圖 S1–S8 未取得。

## [2026-10-25] ingest | Hige et al. 2015, Neuron（MB 輸出突觸的異突觸可塑性）

新增 [[s-hige-2015-heterosynaptic-plasticity]]，圖 7 張。冷讀 4 輪（上限），最後一輪的 3 項已改寫但未再驗證。單篇自身不一致 7 項。補充資料（含 P.I. 公式、圖 S1–S7）未取得。

## [2026-10-25] ingest | Tomchik & Davis 2009, Neuron（KC 內 cAMP 的協同與時間窗）

新增 [[s-tomchik-2009-camp-dynamics]]，圖 7 張。冷讀 2 輪後無「看不懂」。單篇自身不一致 11 項。補充資料未取得。

## [2026-10-25] lint | 建庫

自母庫 `research_with_AI` 移植規範與工具：`CLAUDE.md`（範圍改為果蠅蘑菇體、授權改為私有 repo、網站改本機 8788 埠）、`docs/thematic-page-rules.md`、`.claude/skills/ingest-paper/`、`tools/`（scan、links、build_site、serve）。`papers/` 放入三篇，登記為待處理。
