---
title: hemibrain 連結體資料集（hemibrain）
created: 2026-11-13
updated: 2026-11-24
tags: [entity, active, cross-domain]
confidence: medium
---

# hemibrain 連結體資料集（hemibrain）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **連結體（connectome）**：用電子顯微鏡（電顯）逐一追蹤神經元、畫出的接線圖，可數出兩顆細胞之間有幾個突觸。
- **neuPrint、neuprint-python**：neuPrint 是查詢 hemibrain 的網站；neuprint-python 是從程式查詢它的工具。
- **KC、MBON、DAN**：蕈狀體（mushroom body）裡代表氣味的 Kenyon 細胞；讀出 KC 訊號的輸出神經元；送出多巴胺、代表獎賞或懲罰的多巴胺神經元（PAM 群多為獎賞、PPL1 群多為懲罰）。見 [[e-kenyon-cell]]、[[e-mbon]]、[[e-dopaminergic-neuron]]。
- **區室（compartment）**：KC 軸突排成的幾條「葉」沿長度切成的一格一格，例如 α1、γ1pedc；細胞以所在區室命名（[[c-mb-compartment]]）。
- **型名（例如 SMP354）、編號（例如 MBON07）**：hemibrain 的型名多以所在腦區開頭（SMP＝上內側前大腦）；MBON07、PAM11 這類是它給的編號，Yamada 2023 對照為 MBON07＝MBON-α1、PAM11＝PAM-α1。
- **傳遞物質預測**：用訓練好的神經網路，從突觸的電顯影像判斷它用哪一種神經傳遞物質。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值。

## 是什麼

**hemibrain 是一份以電顯重建的成年果蠅半腦連結體（Scheffer et al. 2020），經 neuPrint 網站查詢。** 庫內七篇用它：兩篇模型拿它定接線或分區，三篇拿它找實驗中的細胞彼此怎麼接，一篇**只拿它當第二隻腦的對照**，還有一篇**以這份資料集本身為研究對象**（[[s-li-2020-mb-connectome]]，見下表）。它只涵蓋半邊中央腦（Minnick 2026 的說明），而且庫內兩篇（Aso 2023、Yamada 2023）只用右半腦，Yamada 2023 的理由是左半腦重建不完整。Aso 2014a 寫成時它還不存在，該篇來源頁只在限制中提到「要到 2020 年的 hemibrain 才能回答哪些重疊是真突觸」，沒有使用。

## 版本與規模

| 來源 | 寫明的版本 | 用到的範圍 |
|---|---|---|
| Huang 2024 | v1.2.1 | γ1、α2、α3 三個模組的九神經元接線 |
| Pribbenow 2022 | v1.2.1（neuprint-python） | 只取狀態為 Traced 的 KC，接到 M4、M6、α′3 三型 MBON 者 |
| Yamada 2023 | 只給資料集 DOI 10.25378/janelia.12818645.v1，未寫版本號 | 右半腦；396 型中間神經元（與 MBON 及 DAN 合計至少 100 個突觸） |
| Aso 2023 | 未寫（該頁標 ？待查） | 右半腦；與 UpWiN 任一顆有 ≥ 20 個連結的上下游 |
| Minnick 2026 | 未寫 | 只用它的區室對應表；模擬本身跑的是另一份連結體 BANC |
| Ganguly 2024 | 未寫版本號（該頁標 ？待查） | 只當**對照**資料集：把 FlyWire 左半腦的視覺投射神經元與局部視覺中間神經元轉到 JRC2018F 模板後，用 NBLAST 對 hemibrain 全庫比對（對到的是 hemibrain 右半腦） |
| Li 2020 | **v1.1**（寫明；論文另承諾該版本永久保留） | 右半腦；蕈狀體相關的整塊——蕈狀體內有分枝的神經元、MBON 的下游、DAN 的上游 |

**整份資料集約 22,500 顆神經元**（[[s-li-2020-mb-connectome]] 正文引 Scheffer et al. 2020）。**這是整個 hemibrain 的數，不是蕈狀體的**：其中約 **2,600 顆**在蕈狀體內有軸突或樹突，約 **1,500 顆**在 MBON 下游（門檻 10 個突觸），約 **3,200 顆**在 DAN 上游（門檻 5 個突觸），Li 2020 說這三者合計約占中央腦神經元的三分之一。**整份資料集有多少突觸，庫內仍沒有任何來源頁寫出：？待查。** 各篇引用的數字見 [[numbers]]（Pribbenow 2022、Aso 2023、Yamada 2023、Minnick 2026 各節）。

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-huang-2024-dopamine-memory-dynamics]] | 依 v1.2.1 定模型接線，兩神經元間少於 5 個突觸設為 0；非零權重全由擬合決定，不參考突觸數 | 接線顯示 γ1pedc 的 MBON 有一條抑制性連線接到 α3 的 DAN，作者據此推論並檢驗「訓練後它放鬆對 α3 DAN 的抑制」 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | v1.2.1，對每個接到 M4、M6、α′3 MBON 的 KC 釋放點，數它同時接到幾個突觸後對象 | 眾數 3–4 個，比例約 0.30–0.35（※ 從圖判讀）；共同接收者含其他 KC、MBON、DAN、[[e-apl-neuron]] 與 [[e-dpm-neuron]] |
| [[s-yamada-2023-second-order-conditioning]] | 右半腦查 MBON-α1 到 DAN 的兩跳路徑，配合傳遞物質預測；並以 hemibrain 的型別細胞總數當作品系涵蓋率的分母 | 主路 MBON-α1 →（SMP353／SMP354）→ SMP108 → 多型獎賞 DAN，兩層都是乙醯膽鹼性；品系標到的細胞數對 hemibrain 總數：α1 5／7、γ5＋β′2a 16／30、β1＋β2 12／22、γ4 11／23 |
| [[s-aso-2023-upwind-neurons]] | 以 MCFO 單細胞影像（[[e-mcfo]]）比對 hemibrain 神經元，找出品系 SS33917 標到的細胞並查其上下游 | 對到 11 顆、5 型：SMP353（1）、SMP354（3）、SLP400（3）、SLP399（2）、SMP348（2）；MBON-α1 → SMP354 共 268 個突觸 |
| [[s-minnick-2026-untrained-connectome]] | 借用 hemibrain 的區室圖，決定 BANC 模型中哪些 KC→MBON 連結可塑 | 可塑的是嫌惡區室的 8,377 條（MBON11–14、16–20、23、25、28、30、32–35，共 50 顆） |
| [[s-li-2020-mb-connectome]] | **本庫唯一一篇以這份資料集本身為研究對象的來源**（其餘六篇都是拿它當工具查某條線在不在）。把 hemibrain:v1.1 裡與蕈狀體有關的那一整塊撈出來重新分型、數連結，並自陳資料的缺陷 | 整份資料集約 22,500 顆神經元；KC 重分成 14 個亞型共 1,927 顆（[[e-kenyon-cell]]）；MBON 從 22 型改成 34 型（[[e-mbon]]）；15 個區室底下有 40 個 DAN 亞型／功能群（[[c-mb-compartment]]）；MBON 下游約 1,550 顆、其中約 600 顆收兩型以上 |
| [[s-ganguly-2024-visual-inputs-to-kc]] | 本庫**第一篇把 hemibrain 當對照、而非主資料集**的來源。主資料是 FlyWire 全腦；hemibrain 用來檢查「主要視覺輸入在第二隻腦裡是不是同一批」 | 66% 的 VPN／LVIN 找到 NBLAST > 0.5 的對應（⚠️ 此比例與該篇圖 7A 的直方圖對不上，見該頁問題與限制第 8 條）；兩份資料的突觸數「高度相關」但**論文沒給相關係數或 p 值**；hemibrain 的 KCγ-d 只有 99 顆，FlyWire 右半腦有 148 顆 |

## 已知的問題

- **重建完整度在腦區之間差很多，而差的那一半正是蕈狀體以外的部分。**（[[s-li-2020-mb-connectome]] 自陳，**引用 hemibrain 時最該打折的一條**）蕈狀體葉內的校對極為徹底：**超過 80% 的電腦預測突觸被指派給了已辨識的神經元**；但原文緊接著寫「in other brain regions, where MBON outputs and DAN inputs lie, reconstruction was often much less complete」，在那些區域**無法估計被標出的突觸能代表多少真實連結**。這削弱的是哪一類引用：凡是**數「某顆細胞在蕈狀體之外收到誰的輸入」或「MBON 的輸出落在哪些腦區」**的結果都要打折——Li 2020 自己約有一半的結果落在這一邊（DAN 的上游分析、MBON 的輸出腦區分布、MBON→扇形體、MBON→下行神經元）；而**只數葉內連結**的結果（KC→MBON、DAN→KC、區室內部的接線）不受這一條影響。庫內既有的引用裡，Yamada 2023 的 MBON-α1→中間神經元→DAN 兩跳路徑與 Aso 2023 的 UpWiN 上下游都落在葉外，屬於要打折的一類。
- **只用右半腦。** Yamada 2023 的 SMP108 左右各一顆、軸突跨到對側（圖 4E、F），但連結數只取自右半腦，跨側輸入在資料裡看不到；行為與生理實驗卻是雙側的腦。[[s-li-2020-mb-connectome]] 的理由寫得最明確：**左半腦的連結不完整**，所以它的 DAN 上游分析與全部亞型分群都只用右半腦。
- **只取 Traced 的細胞會低估。** Pribbenow 2022 排除未完成追蹤的 KC，夥伴數可能偏低（※ 推論：重建不完整只會漏算，不會多算；該篇未討論）。
- **拿 A 資料集的分區表標 B 資料集。** Minnick 2026 用 hemibrain 區室圖選 BANC 的可塑連結，兩者型別是否一一吻合，該篇沒有交代：？待查。
- **接線不等於權重。** Huang 2024 只用 hemibrain 決定「接不接」，強弱全靠擬合；不能把該模型的權重讀成突觸數的結果。
- **型別細胞數當分母要小心。** Yamada 2023 的「5／7」是本庫推論的讀法（※ 推論，見該頁）：品系標到 5 顆、hemibrain 該型共 7 顆。
- **沒有重建視葉，所以視覺輸入的身分查不出來。** [[s-ganguly-2024-visual-inputs-to-kc]] 的引言明說：先前用 hemibrain 做的分析能看出有視覺投射神經元伸進蕈狀體萼部，**但因為視葉沒有重建，那些神經元是誰無法確定**。這是該篇改用 FlyWire 全腦連結體的直接理由，也獨立支持本頁「只涵蓋半邊中央腦」的寫法。**但這句話要帶上 [[s-li-2020-mb-connectome]] 自己的分寸，否則會過強。** 該篇寫小葉（LO）大致包含在 hemibrain 裡、髓質（ME）不在，並緊接著說「**在許多情況下，我們能夠藉由把神經元片段與它們在 FAFB 或光學顯微影像中的完整對應體比對，來確定地標註髓質視覺投射神經元**」——它的圖 10 圓餅只把 0.9% 歸為「無法判定來自髓質或小葉」、1.6% 歸為「離開體積、身分未定」。**然而同一段緊接著寫「we have little definitive insight into the type of visual information conveyed by their VPN inputs.」** 兩句合起來是：**來源腦區確認到了，細胞身分與它們在傳什麼視覺訊息沒有。** 引用時不要只取一半。
- **食道下區（SEZ）也不在體積內。** [[s-li-2020-mb-connectome]] 說 SEZ 是 DAN 輸入的主要來源之一，而 SEZ 輸出神經元的樹突形態只能去 FAFB 補。
- **已辨識的下行神經元只有一小部分。** [[s-li-2020-mb-connectome]] 的圖 42 圖說：hemibrain v1.1 只辨識出**約 15% 的下行神經元、約 50 個型**（同篇正文另一處寫「at most one-third」，⚠️ 單篇自身不一致）。任何「只有某某下行神經元收到某輸入」的陳述，分母都只有這一小部分。
- **版本不一。** 七篇中只有三篇寫明版本（兩篇 v1.2.1、Li 2020 為 v1.1）；其餘四篇的突觸數無法確定與 v1.2.1 可比。

## 相關

- 另一套連結體與工具：[[e-fafb]]（另一份成蟲全腦電顯體積）、[[e-neuprint]]（查詢 hemibrain 的介面與 Neo4J 後端）、[[e-catmaid]]（FAFB 與幼蟲電顯的追蹤平台）、[[e-nblast]]、[[e-mcfo]]
- 細胞：[[e-mbon-alpha1]]、[[e-mbon-gamma1pedc]]、[[e-kenyon-cell]]、[[e-apl-neuron]]、[[e-dpm-neuron]]
- 概念：[[c-second-order-conditioning]]、[[c-sparse-coding]]、[[c-neurotransmitter-prediction]]
- 主題：[[t-mbon-dan-feedback]]、[[t-mbon-to-action]]
- 來源：[[s-li-2020-mb-connectome]]（**以這份資料集本身為研究對象**）、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-yamada-2023-second-order-conditioning]]、[[s-aso-2023-upwind-neurons]]、[[s-minnick-2026-untrained-connectome]]、[[s-ganguly-2024-visual-inputs-to-kc]]（當對照資料集）、[[s-aso-2014-mb-architecture]]（只提及）
- 待開頁面：`e-banc`、`e-flywire`（[[e-fafb]]、[[e-neuprint]]、[[c-neurotransmitter-prediction]] 已開頁，移到上面各列）
