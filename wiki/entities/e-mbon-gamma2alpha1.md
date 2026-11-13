---
title: MBON-γ2α′1（γ2α′1 輸出神經元）
created: 2026-10-25
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# MBON-γ2α′1（γ2α′1 輸出神經元）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ2、α1）；細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **DAN、PAM、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PAM 群多傳遞獎賞，PPL1 群（Handler 2019 寫作 PPL）多傳遞懲罰。
- **MBON**：蕈狀體輸出神經元，接收 KC 的訊號、推動果蠅靠近或走開；學習改變的是 KC→MBON 突觸的強弱。
- **CS+／CS−、順向／逆向**：訓練時配了糖、電擊或 DAN 活化的氣味（CS+），與沒配的對照氣味（CS−）。順向配對＝氣味先、多巴胺後；逆向配對＝多巴胺先、氣味後。
- **PI（表現指數）、LI（學習指數）**：行為分數。一群果蠅在兩種氣味間選擇，換算成一個數；多數篇落在 −1 到 +1（Hige 2015 的刻度不同），0＝沒有偏好，正負號的意思各篇不同（見 [[c-performance-index]]）。
- **消退、再鞏固**：學會後再聞 CS+ 卻沒有糖或電擊，學到的反應減弱，叫消退（[[c-memory-extinction]]）；記憶被叫出來後暫時變得不穩定、再重新存好，叫再鞏固（[[c-memory-consolidation]]）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系。GAL4 與 LexA 是兩套互不干擾的開關；split-GAL4 把 GAL4 拆成兩半（AD 與 DBD），兩半都在的細胞才有作用（[[e-split-gal4]]）。基因型寫「X/+」表示只帶一個品系的對照組。
- **活化與阻斷工具**：CsChrimson 照紅光讓神經元放電（[[e-cschrimson]]）；P2X2 遇到 ATP 讓神經元放電（[[e-p2x2]]）；shibire^ts1（shi）升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]），全程維持低溫的「允許溫度對照」用來排除品系本身的效果。
- **讀數與製備**：ΔF/F0＝螢光相對刺激前基線的變化比例（0.5＝亮了 50%），以遇鈣變亮的 GCaMP 量神經元活動（[[e-gcamp]]）；離體＝把腦取出泡在養液裡做實驗（[[c-ex-vivo-explant]]），活體＝活果蠅固定後打開頭殼看。
- **電壓成像、放電率**：電壓成像（voltage imaging）是用會隨膜電壓變亮變暗的螢光蛋白（Huang 2024 用 pAce）、每秒拍 1,000 張，看得到每一次放電；放電率＝每秒放電幾次。
- **舊名與新名**：Aso 2014a（[[s-aso-2014-mb-architecture]]）以前，蕈狀體的細胞型多用 Tanaka 2008 的舊名（MB-MP1、MB-V2α 等），同一顆細胞在不同論文裡名字不同；Aso 2014a 改以所在區室命名，並在表 1 給出新舊名對照。
- **光遺傳篩檢（Aso 2014b）**：在沒有訓練、沒有氣味時用紅光活化某型 MBON，看果蠅往照光區靠近還是走開；一條品系常同時標好幾型，只標一型就顯著的才算單型證據。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「text.txt 第 N 行」＝本庫保存的論文全文文字檔的行號；「該頁」指表格同一列的來源頁。

## 是什麼

蕈狀體輸出神經元（[[e-mbon]]）的一型，名字串了兩個區室：γ2（γ 葉第 2 格）與 α′1（α′ 葉第 1 格）。這表示它的樹突同時伸進這兩格：命名規則出自 Aso 2014a 表 1（MBON 後面接樹突所在的區室名），該篇圖 8A 也以它為例說明。依 Aso 2014a：每半腦 **2 顆**形態相同、以 MCFO 分不開的細胞（圖 8A–B），乙醯膽鹼性（推定），投射到 CRE 與 SMP（圖 16B）；表 1 沒有給它舊名。同一格的多巴胺神經元是 [[e-ppl1-gamma2alpha1]]（舊名 MB-MV1）。它在本庫兩條研究線上都出現：Hige 2015 拿它當「鄰格」，檢查 γ1pedc 的學習會不會越界；Felsenberg 2017 發現它是糖記憶「再鞏固」（被叫出來的記憶重新存好，見 [[c-memory-consolidation]]）所需的 MBON。

## 版本與規模（標記它的品系）

| 來源 | 品系 | 來源怎麼稱呼 |
|---|---|---|
| Aso 2014a | 表 1：MB077B、MB051B、MB090C；圖 11 的雙色標記中 R25D01-LexA 標的是 γ2 格的 MBON | MBON-γ2α′1（MBON-12） |
| Aso 2014b | MB077B、MB077C（兩者 AD 半都是 R25D01、DBD 半是 R19F09，只差插入位置）；MB051B、MB090C（依表 2 另弱標 MBON-α′2）；R25D01-LexA（影片 6 圖說：標乙醯膽鹼性的 MBON-γ2α′1） | MBON-γ2α′1 |
| Hige 2015 | R25D01-LexA | MBON-γ2α′1 |
| Felsenberg 2017 | MB077C-GAL4（阻斷、光活化）、R25D01-LexA（光活化）；延伸圖 6k、6p 說兩者都標 MBON-γ2α′1 | γ2α′1 MBON |
| Handler 2019 | 25D01-Gal4、25D01-LexA | 「γ2 MBON」 |
| Cohn 2015 | 主文沒寫品系名（？待查） | 「γ2 MBON」 |
| Huang 2024 | split-GAL4，各型品系對照在延伸表 1，未印出（？待查） | MBON-γ2α′1 |

※ 推論：Handler 2019 的「γ2 MBON」就是 MBON-γ2α′1。依據：三篇都用 25D01 這段調控序列，而 Felsenberg 2017 明說 R25D01-LexA 標 MBON-γ2α′1，Aso 2014b 影片 6 圖說也寫 R25D01-LexA 標 MBON-γ2α′1、表 2 的 MB077B／MB077C 都以 R25D01 為一半；不確定之處：GAL4 與 LexA 版本的表現範圍不一定相同，Handler 沒有比對。Cohn 2015 的「γ2 MBON」只以區室命名、品系未知，是否同一型更不確定（？待查）。

## 庫內誰用了它

| 來源 | 怎麼用 | 看到什麼 |
|---|---|---|
| [[s-aso-2014-mb-architecture]] | 命名與形態的原始出處（表 1、圖 8A–C、16B） | 每半腦 2 顆、乙醯膽鹼性（推定）；是正文「乙醯膽鹼型 MBON 在垂直葉」這條通則的例外（樹突有一半在水平的 γ 葉）；末梢與 PAM-β2β′2a 的樹突重疊（圖 20，跨格，只是影像重疊） |
| [[s-aso-2014-mbon-valence]] | CsChrimson 光遺傳活化（MB077B、MB090C、MB051B，未訓練、無氣味）；shibire^ts 阻斷（MB077B、MB051B 等）；dTrpA1 睡眠篩檢（MB077C、MB051B、MB090C） | 活化 → **推動靠近**（MB077B \*\*\*、MB090C \*、MB051B 不顯著）；2 小時獎賞氣味記憶需要它（MB051B、MB077B 兩條）；24 小時酒精記憶只有 MB077B 顯著、MB051B 不顯著；活化增加睡眠（初篩 MB077C、MB051B、MB090C；前兩條複篩重現，MB090C 是否複篩論文沒交代） |
| [[s-hige-2015-heterosynaptic-plasticity]] | 在 γ1 區誘發突觸變弱後，用電極記錄鄰格的它 | 放電約 105 → 91（從圖判讀，n＝6），無效果 → 多巴胺作用沒越界（陰性結果的替代解釋見 [[c-mb-compartment]]） |
| [[s-felsenberg-2017-re-evaluation]] | 糖訓練後再聞 CS−（沒配糖的氣味）時以 [[e-shibire-ts]] 阻斷；離體光活化；活體鈣成像 | 阻斷後再鞏固受損（PI 約 0.12，對照約 0.25／0.265）；3 小時測驗時阻斷它，果蠅也表現不出記憶（PI 約 0.045）；離體光活化它，MB-MV1（PPL1-γ2α′1）的 ΔF/F0 由約 0.03 升到約 0.72、γ5 的 PAM 由約 0.01 升到約 0.53；訓練後對 **CS−** 的反應變大（兩種氣味分派方式分別約 +14% 與 +24%，相對假訓練組），CS+ 不變 |
| [[s-handler-2019-dopamine-receptor-timing]] | 離體配對（73F07-LexA 的 γ2 DAN ＋ P2X2）與真電擊實驗 | 論文說 γ2 也有類似 γ4 的雙向改變；資料在補充圖 S3（？待查，補充資料未取得） |
| [[s-cohn-2015-coordinated-neuromodulation]] | 「γ2 MBON」：離體活化 γ2 DAN、活化 58E02 DAN；活體氣味成像；P2X2 活化它本身 | 活化 γ2 DAN 時 ΔF/F0 約 0.5 → 4.8；活化 58E02 DAN 時約 0.8 → 0.6（不顯著）；活體對氣味的反應約 0.9，遠大於 γ4 的約 0.2；活化它會改變各格 DAN（見 [[t-mbon-dan-feedback]]） |
| [[s-huang-2024-dopamine-memory-dynamics]] | 頭固定、腳踩小球的活果蠅上以電壓成像量放電；不在九神經元模型內 | 自發約 22 次／s（※ 從圖判讀）；6 回合電擊訓練（CS+ 與 CS− 都是吸引氣味）後對 CS+ 的反應下降、1 小時後接近恢復，與 MBON-γ1pedc>α/β 同屬短期改變 |

## 已知的問題

- **CS− 反應變大，現有規則沒有涵蓋。** 庫內的突觸規則都只處理「與多巴胺配對的氣味」；Felsenberg 2017 的變大發生在沒配糖的氣味上，來源沒有解釋（見 [[syn-contradictions]] 3.7）。
- **再鞏固與記憶表現分不開。** 它同時是表現記憶所必需，阻斷時果蠅可能根本叫不出記憶（Felsenberg 2017 圖 4b）。
- **光活化在取出的腦裡、沒有氣味時做，n 小**（4、5 筆），只說明「活化它會讓 DAN 鈣上升」，不區分直接或間接連結。
- **「推動靠近」的證據來自 Aso 2014b，而且是少數有單型證據的一型。** Handler 2019 引 Aso 2014b 說 γ2 MBON 推動靠近；回查原文，MB077B、MB090C 兩條只標它（MB090C 另弱標 MBON-α′2）的品系都顯著，第三條 MB051B 不顯著。Aso 2014b 用它與 γ1pedc>α/β 當「MBON 推動方向與同格 DAN 寫入的記憶相反」的例子。
- **Aso 2014b 的「促眠＝靠近」是兩組獨立實驗的類比。** 睡眠用 dTrpA1、MB077C，光遺傳用 CsChrimson、MB077B；兩條品系的兩半序列相同，只是插入位置不同。
- **Huang 2024 的放電數字誤差較大。** 它是六型 MBON 中放電訊號最小、偵測錯誤率最高的三型之一（MBON 錯誤率最高每秒 1.7 次，延伸圖 1l）。
- 跨篇是否同一型細胞，見「版本與規模」的 ※ 推論。

## 相關

- 細胞：[[e-mbon]]、[[e-ppl1-gamma2alpha1]]、[[e-mbon-gamma1pedc]]、[[e-dopaminergic-neuron]]
- 概念：[[c-mb-compartment]]、[[c-memory-consolidation]]、[[c-kc-mbon-plasticity]]
- 主題：[[t-mbon-dan-feedback]]、[[t-memory-updating]]、[[t-mbon-to-action]]
- 來源：[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-felsenberg-2017-re-evaluation]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-huang-2024-dopamine-memory-dynamics]]
