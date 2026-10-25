# 日誌

只追加，新的在最上面。動作僅三種：`ingest` / `query` / `lint`（另有人類的 `裁決`）。

## [2026-10-25] lint | 第二批整合：主題、概念、實體、索引、登記簿

- 新研究問題群「記憶寫入之後：鞏固、更新與迴路回饋」（`index.md` 新 H2，`tags` 值 `mb-memory-dynamics`）。新主題 [[t-memory-updating]]（冷讀 4 輪）、[[t-mbon-dan-feedback]]（冷讀 4 輪）。改寫 [[t-timing-rules]]（冷讀 4 輪）、[[t-dopamine-to-plasticity]]（冷讀 3 輪）。
- 概念頁 7 → 14、實體頁 8 → 25：新開 24 頁（核心 9 頁、選配 5 頁、回查各來源頁待開清單後 10 頁），既有 15 頁全部補「庫內的用法」列。新頁冷讀 1 輪。
- [[syn-contradictions]]：跨來源矛盾 2 → 6 條（新增 1.3 不配對多巴胺的時間尺度、1.4 MB099C、1.5 R58E02-LexA、1.6 γ2 MBON→DAN 的正負號）；1.1 加入 Aso 2016 的並列資料；空缺 5 → 8 條（新增 3.6、3.7、3.8），3.1–3.4 補上新進展；4.1、4.3、4.4 更新；單篇自身不一致索引加五列。
- 更正既有頁：MB099C「四型」（六頁改並列）、R58E02-LexA「γ4–5」（兩頁改並列）、區室獨立性的措辭（三處）、時間尺度二分法、P.I. 正負號約定（六篇）、KC 總數 ？待查回填（Aso 2016、Cohn 2015）。[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]] 加註。
- 八篇來源頁「待開頁面」中已開的名稱改為連結；兄弟篇之間的純文字提及改為實際對照與連結；新來源頁的 `tags` 加上 `mb-memory-dynamics`。
- `numbers.md` 併入五篇的數字節。`index.md`、`intake.md`（五篇改為已收錄）、`README.md`（閱讀順序、全頁目錄、圖片授權分兩類）。[[syn-changelog]] 加階段三，更正清單加 25 處，新開癸、子兩類。

## [2026-10-25] ingest | Felsenberg et al. 2018, Cell（嫌惡記憶的消退：並行的相反記憶）

新增 [[s-felsenberg-2018-memory-extinction]]，圖 7 張，CC BY 4.0。冷讀 3 輪後無「看不懂」。單篇自身不一致 8 項＋輕微 2 項。表 S1（全部 n 與 p 值）未取得。

## [2026-10-25] ingest | Felsenberg et al. 2017, Nature（獎賞記憶的消退與再鞏固）

新增 [[s-felsenberg-2017-re-evaluation]]，圖 4 張（延伸圖未收）。冷讀 4 輪（上限），最後一輪 2 項已改寫未再驗證。單篇自身不一致 7 項。新矛盾：R58E02-LexA 的標記範圍。

## [2026-10-25] ingest | Aso & Rubin 2016, eLife（各型 DAN 的寫入與更新規則）

新增 [[s-aso-2016-dan-cell-type-rules]]，圖 5 張，CC BY。冷讀 4 輪後無「看不懂」。單篇自身不一致 6 項。新矛盾：MB099C 標記幾型 DAN。

## [2026-10-25] ingest | Ichinose et al. 2015, eLife（PAM-α1／MBON-α1 迴圈與獎賞型長期記憶）

新增 [[s-ichinose-2015-reward-recurrent-circuit]]，圖 11 張，CC BY。冷讀 4 輪（上限），最後一輪 2 項已改寫未再驗證。單篇自身不一致 9 項。

## [2026-10-25] ingest | Cohn, Morantte & Ruta 2015, Cell（DAN 網路協調與分區的 KC→MBON 調節）

新增 [[s-cohn-2015-coordinated-neuromodulation]]，圖 7 張。冷讀 4 輪後無「看不懂」。單篇自身不一致 8 項。新矛盾：不配對多巴胺 > 45 s 增強 vs Handler 2019 的 6 s 幾乎不變。補充資料未取得。

## [2026-10-25] lint | 改為公開網站

依使用者決定：全文改連 PMC、PDF 不進 git、原圖逐圖標出處。三篇來源頁的 citation 與資料表「出處」列改為 PMC 連結，本機 PDF 檔名移到隱藏註解；`tools/scan.py` 改讀註解；21 張圖加出處行；`.gitignore` 排除 `papers/*.pdf`，第一個 commit 改寫為不含 PDF；`tools/build_site.py` 不再連結 `papers/`；新增 `.github/workflows/pages.yml`；`CLAUDE.md`、`papers/README.md`、頁面規格、範本、`README.md` 同步。[[syn-changelog]] 加階段二。

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
