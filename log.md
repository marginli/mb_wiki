# 日誌

只追加，新的在最上面。動作僅三種：`ingest` / `query` / `lint`（另有人類的 `裁決`）。

## [2026-11-13] lint | 第一批補跑冷讀（5 頁完成，7 頁未跑）

第一批 11 篇收錄時依使用者決定跳過冷讀，之後使用者要求補跑。一頁一個主持代理，照 cold-read skill 切區塊、每輪派全新冷讀者、改寫後用 check_facts.py 驗數字與引用。

**已完成 5 頁**（數字與引用零消失，「圖／相關／出處／論文摘要」逐字未動）：
[[t-mbon-to-action]]、[[t-innate-learned-integration]]（各 3 輪＋1 輪驗收＋1 輪定點改寫）、[[s-mao-2009-dopaminergic-neuron-types]]（2 輪）、[[s-aso-2014-mb-architecture]]（3 輪）、[[s-burke-2012-octopamine-dopamine-reward]]（輪數不詳，代理回報前額度用盡）。

**冷讀抓到的事實錯誤（已改正）：**
- 兩條主題頁：導言把「MBON 本來就抑制迎風神經元」與「學習讓抑制變鬆」壓成一句，讀者建立相反模型；單隻頭部固定的虛擬軌跡被誤寫成「一盒 4–7 隻的整盒重心」（那是另一套裝置）；表格「10 個基因型」與正文「9 個基因型加 1 個對照」矛盾；摘要「三篇」實為四篇；幼蟲 62 型匯聚神經元被寫得像「兩邊下游的交集」（實為三種形式 14＋4＋44 相加）；「三個齡期拼成」更正為一齡與三齡。
- Mao 2009：把「圖上沒標」當成「不顯著」；「電擊似乎抵銷了部分下降」改標為推論並寫出反例。四處明寫「功能成像只做四段，沒有量過 γ1pedc」（空缺 3.20 的基礎）。
- Aso 2014a：改掉「空間分開＝功能分開」這個與「功能完全未測」衝突的宣稱；更正討論裡兩篇論文走同一條路的敘述；「12 個受測交界中的 11 個」改成 12 個交界、11 個確認、1 個缺品系沒測。新增 ⚠️ 單篇自身不一致：同一型細胞在圖 5 寫 `PAM-γ4>γ1γ2`、另三張圖寫 `PAM-γ4<γ1γ2`。

**方法上的兩個教訓：**
1. 主持代理自評「看不懂已清零」不可信。兩條主題頁補派驗收讀者後，仍找出 5 項看不懂與 3 處事實錯誤。**驗收輪列為必要程序。**
2. 平行跑的代理共用 scratchpad 的 `chunks/` 會互相覆蓋（Aso 2014a 的第二輪成品全毀、無副本，只能從原檔重建）。**每個代理一定要指定專屬子目錄。**

**未跑冷讀的 7 頁**（代理在額度用盡時中斷，都還沒寫回原檔，頁面維持收錄時的狀態）：Aso 2014b、Dylla 2017、Aso 2019、Eschbach 2021、Pribbenow 2022、Aso 2023、Yamada 2023、Kaldun 2025。

## [2026-11-13] ingest | 第一批 11 篇（learning_memory_fly.docx 參考文獻）

使用者要求下載 learning_memory_fly.docx 參考文獻中可合法取得的全文：117 篇中抓到 33 篇；範圍外 7 篇（全腦連結體與身體模擬 6 篇、撤稿 1 篇）依使用者裁示不收錄、未放入 papers/；26 篇放入 papers/，其中第一批 11 篇收錄（區室與回路、學習的訊號機制），其餘 15 篇待處理。

**新增來源 11 篇：** [[s-mao-2009-dopaminergic-neuron-types]]、[[s-burke-2012-octopamine-dopamine-reward]]、[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-eschbach-2021-learned-innate-valence-integration]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-aso-2023-upwind-neurons]]、[[s-yamada-2023-second-order-conditioning]]、[[s-kaldun-2025-dop1r2-memory-phases]]。每篇由一個收錄代理平行撰寫，`numbers.md` 併入 11 段。

**冷讀：** 冷讀途中多個子代理被 Anthropic 安全機制中斷（標為生物研究相關），使用者決定本批跳過冷讀。Dylla、Mao、Kaldun 三篇已併入中斷前完成且核對過數字與引用的改寫；Burke 2012 依主持代理回查原文的 4 處事實更正已改入。其餘各篇未經冷讀。

**主題頁：** 新開 [[t-mbon-to-action]]、[[t-innate-learned-integration]]（使用者同意）。[[t-dopamine-to-plasticity]] 整合 9 篇；換模型後補完 [[t-mbon-dan-feedback]]（維護註記已刪）、[[t-timing-rules]]、[[t-memory-updating]]。

**整合時發現的跨篇關聯：** Yamada 2023 的中介層 SMP353／SMP354，就是 Aso 2023 命名的迎風神經元（UpWiN）——同一群細胞，在 Aso 2023 是把價值變成迎風動作的解碼器，在 Yamada 2023 是把一格的記憶送去教另一格的中繼站。兩個角色不互斥，但沒有人在同一個實驗裡同時量過。已寫入 [[t-mbon-dan-feedback]]。

**概念與實體：** 新開 15 頁（[[e-mbon-alpha1]]、[[e-mbon-alpha3]]、[[e-ppl1-alpha3prime]]、[[e-catmaid]]、[[e-hemibrain]]、[[e-mcfo]]、[[e-grasp]]、[[e-apl-neuron]]、[[e-dpm-neuron]]、[[c-appetitive-memory]]、[[c-valence-coding]]、[[c-prediction-error]]、[[c-nonassociative-learning]]、[[c-feedforward-inhibition]]、[[c-second-order-conditioning]]）；換模型後補建 [[e-ok107-gal4]]、[[e-c305a-gal4]]、[[e-gal80ts]]、[[e-vt1211]]、[[e-dtrpa1]]、[[e-tnt]]（e-gal80ts 兩篇都做了實驗，但 Kaldun 2025 的圖在未取得的補充資料裡，頁內已註明；主持者裁示保留）。既有概念與實體頁的「庫內的用法」由整合代理補列。

**矛盾清單：** 新增 1.10（*rutabaga* 能否解釋痕跡制約）、1.11（只聞氣味是否讓 PPL1 反應下降，前提待確認），待裁決 9→11；1.9 補 Aso 2019、1.3 補 Pribbenow 2022；4.4 依 Aso 2014a 部分解決；單篇自身不一致索引補 11 篇。空缺 3.2（分成獎賞／嫌惡兩半讀）、3.6（Yamada 2023 填掉一半）已更新；新增空缺 3.16–3.20（DAN 習得反應來源、γ 葉是否需要 Dop1R2、MBON-α1 的麩胺酸對兩個下游各做什麼、二選一分數高卻不迎風、懲罰把各型 PPL1 活化到什麼程度）；空缺 15→20 條。4.1 補上第一批補充資料全未取得。查證兩點：Aso 2023 的 γ4 迎風弱不構成矛盾（PI 最低、檢定力不足），乾淨的分離在 γ5β′2a；Aso 2019 圖 9C 的前提引 Mao 2009，但 Mao 2009 沒有量過 γ1pedc。

**既有概念與實體頁（代理 C）：** 約 30 頁已補列；換模型後補完其餘 10 頁（[[c-octopamine-reward-signal]]、[[c-performance-index]]、[[c-us-substitution]]、[[c-kc-mbon-plasticity]]、[[c-mb-compartment]]、[[c-memory-extinction]]、[[e-gcamp]]、[[e-cschrimson]]、[[e-shibire-ts]]、[[e-olfactory-arena]]），主持者另補 [[c-presynaptic-calcium]]（Dylla 2017 的 KC 軸突鈣，含「突觸前是從量測位置推來的」與基線漂移兩條陷阱）。pedc、sc 字尾的寫法經回查 Aso 2014a 已一致（該篇表 1 與圖 10–13 有定義），不需再統一。

**整合時查出、值得記住的落差：** 蕈狀體的「格數」在庫內至少有五個數字（15、16、11–12、9、13），因為各篇量的範圍與層級不同，已寫進 [[c-mb-compartment]]；[[c-performance-index]] 的公式在庫內有 16 種寫法，Kaldun 2025 換裝置就換公式；限制溫度本身會讓實驗做不成（Yamada 2023 在 32 °C、Aso 2023 的對照不迎風），已寫進 [[e-shibire-ts]]。

**來源頁連結整理（換模型後補做）：** 待開清單 13 檔改成連結（含 `c-reward-prediction-error` 由 [[c-prediction-error]] 取代）；正文交叉連結 19 檔 46 組補齊，重跑比對腳本剩 0 組；22 檔的「相關」節補登漏列的來源與兩條新主題頁。

**其他頁的更正：** 依 Aso 2014b 更正 Handler 2019 頁（γ5 MBON 推動走開）、Ichinose 2015 頁（前人集中在提取、MBON-α1 推動走開）三處；「外側角」統一為「側角」；Eschbach 2021 頁一句宣稱唯一性已更正。

## [2026-11-13] ingest | Huang 2024：電壓成像下的 PPL1 價值整合與短期／長期記憶單元的交互

新增 [[s-huang-2024-dopamine-memory-dynamics]]（*Nature* 634:1141–1149，CC BY 4.0），主圖 5 張與延伸圖 13 共 6 張圖；`numbers.md` 新增一段（PPL1 五型與 MBON 六型的自發、電擊、糖放電率，模型時間常數與回饋移除效應，間隔與消退實驗數值）。冷讀 4 輪：看不懂約 20→10→9→2，最後 2 項由主持者直接改寫，未再讀；吃力每塊仍有 3–10 項。

**矛盾清單**：新增 1.9（γ1pedc 在多巴胺先到或被壓低時突觸會不會變強：Huang 2024 模型假設 vs Hige 2015 實測），使用者 2026-11-13 裁示標為跨篇矛盾；待裁決由 8 條增為 9 條。單篇自身不一致索引加一列。4.3 改為十三篇。

**主題頁**：[[t-mbon-dan-feedback]] 新增「第四個難題」一節與證據表一列（第一條有活體活動證據的回饋），篇數改為五篇；[[t-timing-rules]]、[[t-memory-updating]]（新增「消退的時機」一節）、[[t-dopamine-to-plasticity]] 各加一段。

**概念與實體**：18 頁加「庫內的用法」一列；新開 [[e-ppl1-alpha3]]、[[e-ppl1-alpha2alpha2]]、[[e-mbon-alpha2sc]]（皆由本篇湊滿兩篇門檻），Hige 2015 等來源頁的待開清單已改為連結。

**登記簿**：本篇已收錄；同時把 11-12 放入的 Hige 2015 補充檔 `mmc1.pdf`、`mmc2.pdf` 登記為不收錄（暫時擱置，待補寫 Hige 補充資料時改用 `mmc2.pdf`）。

## [2026-11-13] lint | 規則：經使用者要求可下載新 PDF 放入 papers/

`CLAUDE.md` 硬規則「不得改動 `papers/`」加上唯一例外：使用者要求時，Claude 可新增合法免費全文 PDF，放入前先做重複偵測；已有的檔仍不得動。

## [2026-11-12] ingest | Gervasi 2010：活果蠅 KC 內的 PKA（自 10-27 的「處理中」恢復）

[[s-gervasi-2010-pka-dynamics]] 的來源頁與 8 張圖在 10-27 已寫好（冷讀 4 輪），整合未做。依「中斷筆記一律待驗證」，先對照頁面影像抽查圖 6C（*rut2080* 只做了配對組）與圖 7（*dnc1* 的數值），都成立。來源頁補上「本頁用語」表（38 詞），並在 3.4、3.5 節末與討論第 5、6 點標明對應的矛盾編號。

**新開 3 頁**（皆由本篇湊滿兩篇門檻）：[[e-dunce]]（Tully 1985 ＋本篇）、[[e-238y-gal4]]（Tomchik 2009 ＋本篇）、[[c-octopamine-reward-signal]]（Tomchik 2009 ＋本篇）。Tully 1985、Tomchik 2009、[[e-rutabaga]] 的待開清單已改為連結。

**矛盾清單**：新增 1.7（單獨給多巴胺或章魚胺時是否依賴 *rutabaga*）、1.8（章魚胺＋乙醯膽鹼是協同還是次加成），待裁決由 6 條增為 8 條。空缺 3.5 保留編號、註明已轉為 1.8；3.11 補上本篇的部分處理。單篇自身不一致索引加一列（11 項）。4.1、4.3 的篇數改為十二，並刪掉 4.3 一句重複兩次的句子。

更新頁：[[t-dopamine-to-plasticity]]（第二環加 PKA 層級的配對與兩處矛盾、第三環加 Dunce 的空間侷限、缺口兩條改寫）、[[t-timing-rules]]（缺口一條）、[[c-camp-signaling]]、[[c-coincidence-detection]]、[[c-mb-compartment]]、[[c-performance-index]]、[[e-rutabaga]]、[[e-kenyon-cell]]、[[e-mushroom-body]]、[[e-t-maze]]、[[e-dopamine-receptor]]、[[e-epac-camp-sensor]]，另 `index.md`、`numbers.md`（新增一節）、`intake.md`（改為已收錄）、[[syn-changelog]]（階段七；更正清單增 5 處）。

**冷讀兩輪**（新開三頁、主題頁新增的兩段、矛盾 1.7–1.8）：第 1 輪 4 名讀者「看不懂」8 項，第 2 輪 1 名新讀者 0 項。改出兩處實質錯誤：主題頁把 γ 葉也算進「同一顆細胞內部的差別」；1.7 的 EC50 沒標哪篇是哪個、順序與表格相反。另將 1.7 中「補充圖 S4 可確認差別落在 cAMP 與 PKA 之間」收窄為只能確認讀數反映 PKA。`check_facts.py` 數字與引用零遺失（238Y 頁刻意刪去兩個全文行號）。

## [2026-11-12] lint | Minnick 2026 冷讀兩輪

第 1 輪 4 名冷讀者回報「看不懂」23 項、「吃力」57 項；第 2 輪 2 名新冷讀者降為「看不懂」3 項，再修一輪後清零。本頁一開始就帶用語表（從 Tumkaya 那次學到），所以第 1 輪的問題集中在內容而非術語。

冷讀改出的實質更正：

- **科普文自相矛盾。** 原本先寫「調成 0.15 後活化比例落回真果蠅範圍」，又寫「修好後仍有 68%、一樣是密的」。回查原文確認兩句講的是**不同刺激**：窄氣味下校正版 6.1%，場地氣味（驅動每一顆受體神經元，約 120 Hz）下 68%，而學習實驗用的是後者。已在科普文、用語表、3.3、3.4 四處用表格攤開三種刺激條件，並同步修正 [[c-sparse-coding]]。結論因此更銳利：**校正版做出聯結式學習時編碼並不稀疏**，關鍵是「沒有氣味時會不會安靜」（67% 對 4.2%）。
- **圖 1 的中譯沒有對應原文。** 原本「原圖說」只摘一句標題、「圖說中譯」卻有完整 (a)–(f)，而中譯聲明為忠實翻譯。已從 PDF 第 23 頁補上完整原圖說並依原文重寫中譯。
- **「105 型」與「105 顆」不一致**（我方筆誤）。確認為 105 **顆**膽鹼性局部神經元，分屬 11 個**型別**；已全頁統一並在用語表增一條說明。

冷讀另促成三處查證後補入的內容：**價性的算法**（趨近減躲避的脈衝數除以正規化常數，可驗算）、**MBON 正負號的判定方式**（依傳遞物質，104 顆中 75 趨近／25 躲避／4 未定）、**場地氣味的受體驅動率**（120±80a Hz）。這三項都已登記 `numbers.md`。

新增稽核兩項：正文 0.15 mm 與圖 6g 標註 0.2 mm 不一致（單篇自身不一致）；「沉默 APL」實際只關掉兩顆中有型別標註的那一顆。另在 4(d) 補一個論文未點出的理由——MBON05 不在可塑名單上，其突觸本就不會被削弱。

每輪都跑 `check_facts.py`，數字與引用零遺失；篇幅 +32%。

## [2026-11-12] ingest | Minnick 2026：未經訓練的連結體模擬

新增 [[s-minnick-2026-untrained-connectome]]（arXiv 預印本，未經同儕審查，confidence 降為 medium）。**本庫第一篇不做實驗的來源，也是第一篇只收錄一部分的來源**：該篇 42 頁大半在講導航與運動控制，經使用者裁示，來源頁只完整處理蕈狀體與學習的部分，六張主圖重製三張（圖 1、3、6），範圍決定寫在頁首與 `intake.md`。

**新增概念頁 [[c-sparse-coding]]**：本篇與 [[s-hige-2015-heterosynaptic-plasticity]] 使它達到「兩篇來源實際使用」的門檻。Hige 2015 的待開清單已改為連結。

更新 6 頁：[[t-dopamine-to-plasticity]]（新增一節：只有接線時這個機制會怎樣）、[[c-kc-mbon-plasticity]]、[[c-coincidence-detection]]、[[e-kenyon-cell]]、[[e-mushroom-body]]、[[s-hige-2015-heterosynaptic-plasticity]]，另更新 `index.md`、`numbers.md`、`intake.md`、[[syn-contradictions]] 與 [[syn-changelog]]（新增階段六）。

稽核：單篇自身不一致 1 項（方法寫非配對時「Kenyon 細胞會安靜」，同篇圖 3g 顯示 68% 在活動），另有 6 項論文未處理的問題寫在來源頁。新增空缺 2 條（3.14 編碼密度差一個數量級的原因未定、3.15「稀疏是聯結學習前提」未被檢驗），空缺 13 → 15。無新的跨來源矛盾。

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
