# 日誌

只追加，新的在最上面。動作僅三種：`ingest` / `query` / `lint`（另有人類的 `裁決`）。

## [2026-11-12] lint | Tumkaya 2025 冷讀兩輪

第 1 輪 8 名冷讀者（分 8 區塊）回報「看不懂」39 項、「吃力」56 項，根因是本頁漏了庫內其他來源頁都有的「本頁用語」表。補上 28 個詞的用語表（含驅動品系／效應子這組零件關係、Chrimson 與 Chr2XXL 的區別、PI／ΔPI／半 PI、N 在兩台裝置的不同單位、信賴區間的判讀標準），並改寫科普文、結果節、討論與限制、六張圖的解讀。第 2 輪 4 名新冷讀者回報「看不懂」降為 9 項，再修一輪。

冷讀改出兩項實質更正，不只是用詞：

- **圖 1 解讀寫錯一句。** 原寫「不能把 D1 的線段長度當成 D2 的效果量」，但 D1 每條線的垂直落差正是該通道的 ΔPI。已改為說明兩張圖縱軸意義不同（PI 對 ΔPI），而非否定線段長度。
- **圖 3 的結論範圍收窄。** 原寫「ORN 放電的精細時間結構不是學習的必要條件」。冷讀者指出圖 3 測驗時兩半通道都有紅光（連續對 20 Hz 脈衝），而不帶 Chrimson 的 Gr21a 對照 ΔPI 達 −0.37，表示果蠅**光靠視覺**就分辨並學會躲開其中一種閃爍。因此本庫能支持的說法收窄為「**經由 ORN 傳遞的**時間結構學不起來」。已同步 [[t-timing-rules]]、[[c-cs-us-timing]]、[[c-us-substitution]] 與 [[syn-changelog]]。

另補：單隻裝置 WALISAR 的 PI 如何計算，論文未說明，本頁以 ※ 推論標出並標 ？待查。每輪都跑 `check_facts.py`，數字與引用零遺失；篇幅 +37%。

## [2026-11-12] ingest | Tumkaya 2025：全合成記憶植入

新增 [[s-tumkaya-2025-synthetic-memory-inception]]，圖 6 張（CC BY-NC 4.0，逐圖標出處與授權）。本篇無補充圖表，故全頁沒有「補充資料未取得」的待查。

更新 9 頁：主題 [[t-timing-rules]]（新增「刺激自己的節奏」一節，並在缺口補「同時給有多寬容沒人量過」）、[[t-dopamine-to-plasticity]]（新增作者自劃的界線：未直接操作突觸）；概念 [[c-us-substitution]]（新增陷阱 6：取代 CS 的證據強度分方向）、[[c-performance-index]]（新增陷阱 8–10：ΔPI vs PI、半 PI vs 全 PI、不報 p 值不等於沒做統計）、[[c-coincidence-detection]]（陷阱 6–7）、[[c-cs-us-timing]]（陷阱 8–9：兩種「時間結構」別混用）；實體 [[e-r58e02]]、[[e-th-gal4]]、[[e-cschrimson]]（新增 Chr2XXL 段）、[[e-dopaminergic-neuron]]、[[e-t-maze]]（新增 MOT／WALISAR 對照）。另更新 `index.md`、`numbers.md`、`intake.md` 與 [[syn-changelog]]（新增階段五）。

單篇自身不一致 4 項、論文未做的計算或未討論的資料 5 項，全部登記在 [[syn-contradictions]] 第二節與來源頁「五、問題與限制」第 4 條。無新的跨來源矛盾。新增空缺 2 條（3.12 全合成記憶與自然記憶是否相同、3.13 全光學方法尚未用來掃時間差），空缺總數 11 → 13。

判定 `2025-Sexual dimorphism...（MaleCNS 連結體預印本）` **暫不收錄**（使用者裁示），理由與重新考慮的條件寫在 `intake.md` 的「不收錄的判定紀錄」。另登記使用者於同日放入的 `2026-Sensorimotor behaviour from an untrained brain-and-nerve-cord connectome.pdf` 為待處理。

## [2026-11-12] lint | 譯名統一：蘑菇體 → 蕈狀體

依使用者的用語規則，全庫 wiki 頁、`README.md`、`index.md`、`intake.md`、`CLAUDE.md` 與 skill 的「蘑菇體」一律改為「蕈狀體」（約 210 處）。本日誌較早條目照「只追加」原則保留原字。數字、引用與結論未動。

## [2026-11-12] 裁決 | 範圍擴大為果蠅學習與記憶

使用者決定把本庫範圍由「果蠅蕈狀體研究」擴大為「果蠅的學習與記憶研究（不限腦區、含幼蟲與習慣化、敏感化等非聯結式可塑性），以及蕈狀體本身的研究」，不另開新庫。改了 `CLAUDE.md`（範圍段、研究問題群的 tag 命名）、`.claude/skills/ingest-paper/SKILL.md` 的範圍段、`README.md` 與 `index.md` 的標題和開頭介紹。repo 名稱與網址不變；現有 tag `mb-learning`、`mb-memory-dynamics` 不改名。

## [2026-11-09] edit | P.I. 的分母：補「留在中央者算不算」的陷阱

[[c-performance-index]] 新增陷阱 7：分母含不含留在中央的果蠅會算出兩個分數；整理庫內各篇的分母（Tully 1985 ※ 推論含、Felsenberg 2018 ？待查、Aso 2016 競技場無此問題），並提醒模擬或自製裝置的分數（常以已進臂隻數為分母）要先對齊分母才能和 Λ 並排。[[e-t-maze]]「已知的問題」加一條對應說明。沒有新數字（93%／4%／3% 已在 [[numbers]]）。

## [2026-10-27] lint | 全庫「沒頭沒尾」句子檢查

- 使用者要求檢查全庫是否還有類似 Tully 1985 那句沒頭沒尾的句子。59 頁分 8 組逐句檢查（孤立補充句、指涉不明、推理跳步、未定義名詞、缺主詞），共找到 100 處，改寫 41 個檔：來源頁 34 處、主題頁 14 處、概念頁 17 處、實體頁 20 處、[[syn-contradictions]] 6 處、[[syn-changelog]] 7 處、`index.md` 2 處。
- 數字、引用與結論未動。需查原文的項目回查 `.cache/` 抽取文字後才改（Handler 2019 的 IP3 受體推理、Hige 2015 圖 S5 對照、Ichinose 2015 圖 1 的洋紅色標記）；Felsenberg 2017「為什麼怕藥＝在再鞏固」原文無依據，未補。
- 順帶清掉早期留下的過時指涉：[[syn-contradictions]] 的「另兩篇」「三篇」、[[s-felsenberg-2017-re-evaluation]] 的「本頁撰寫時未讀該篇」、[[s-felsenberg-2017-re-evaluation]] 指錯段落的「第三段」。
- 修改段落冷讀 2 輪：第 1 輪兩位讀者另指出 6 處（指涉不明 4、孤立補充句 1、缺主詞 1），已改；第 2 輪重讀這 6 處，再改 2 處（[[e-mbon-gamma5beta2a]] 命名句移回命名處、[[c-memory-consolidation]] 補上提醒的理由），其餘 4 處無「看不懂」。

## [2026-10-26] lint | Tully 1985「為什麼重要」段落改寫

- 使用者指出「缺的是一種受鈣訊號刺激、會製造 cAMP 的酵素」一句沒頭沒尾。改寫 [[s-tully-1985-classical-conditioning]] 該段：先白話說明海兔模型的配對放大（US 啟動腺苷酸環化酶、CS 帶來的鈣讓它更猛），再說 *rutabaga* 失去的是「被鈣催得更猛」的能力，並補上「模型認定學習只來自配對放大」這一步推理；Tomchik 2009 的藥物補註乙醯膽鹼／多巴胺各代替什麼。數字、引用與結論未動。冷讀 1 輪。

## [2026-10-26] ingest | Tully & Quinn 1985, J Comp Physiol A（T 迷宮古典制約與突變株的記憶保留）

- 新增 [[s-tully-1985-classical-conditioning]]，圖 10 張＋表 1 重製，© Springer-Verlag，無免費全文（出處只給 DOI）。掃描版 PDF 無文字層，以 300 dpi 渲染＋tesseract OCR 轉出，數字逐一對照頁面影像校正。全文不提蘑菇體，經使用者同意收錄。
- 先依 skill 預設停點與使用者討論五個關鍵發現，再動筆。
- 單篇自身不一致 4 項（95% vs 93%、循環數「up to four」、「兩氣味影響相同」vs 顯著交互作用、對照組三個 vs 四個）。
- [[syn-contradictions]]：1.1 加入本篇的純逆向（不重疊）資料，裁決條件不變；第二節加一列；新增空缺 3.9（突變株兩段式衰減）、3.10（逆轉訓練的兩種讀法）、3.11（*dnc*／*rut* 與殘餘學習路徑）；4.1、4.3 篇數與說明更新。
- 新開 [[e-rutabaga]]（Tomchik 2009 待開清單，本篇為第二篇來源）。更新主題 [[t-timing-rules]]、[[t-dopamine-to-plasticity]]、[[t-memory-updating]]；概念與實體 [[c-cs-us-timing]]、[[c-memory-extinction]]、[[c-memory-consolidation]]、[[c-camp-signaling]]、[[c-coincidence-detection]]、[[c-performance-index]]、[[e-t-maze]]。
- [[s-tomchik-2009-camp-dynamics]] 圖 6 加入與本篇圖 7 的重做對照、待開清單移除 `e-rutabaga`；[[s-felsenberg-2018-memory-extinction]] 兩處引用改連本篇並註明定義差異。
- `numbers.md` 加 Tully 1985 段（出處用期刊頁碼）。`index.md`、`intake.md`、`README.md` 更新。[[syn-changelog]] 加階段四。

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
