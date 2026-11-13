---
title: 蕈狀體輸出神經元（mushroom body output neuron, MBON）
created: 2026-10-25
updated: 2026-11-13
tags: [entity, active, mb-learning]
confidence: medium
---

# 蕈狀體輸出神經元（mushroom body output neuron, MBON）

## 是什麼

讀取 [[e-kenyon-cell]]（KC）訊號、再把結果送出 [[e-mushroom-body]] 去影響行為的神經元。每型 MBON 的樹突佔據葉上的一個區室（[[c-mb-compartment]]），在那裡收 KC 軸突送來的訊號；同一區室裡另有一型 [[e-dopaminergic-neuron]]（DAN）調整這個「KC → MBON」突觸的強弱。MBON 以所在區室命名，例如 MBON-γ1pedc 的樹突在 γ1pedc 區室。

**價值（valence）**：直接活化不同的 MBON，會讓果蠅靠近或走開。Hige 2015 與 Handler 2019 都引 Aso et al. 2014b 說明這件事；Hige 2015 另引該文說，一般而言 MBON 推動的行為方向，與同區室 DAN 傳遞的價值相反（例如懲罰 DAN 配推動靠近的 MBON）；這條通則在 Aso 2014b 原文只寫到「一般而言」，而且是依傳遞物質分組，有反例（見「已知的問題」）。而懲罰 DAN 放出的多巴胺，會讓同區室 KC→MBON 的突觸變弱（例：Hige 2015 的 γ1pedc，見下表）。因此學到「這個氣味不好」，就是把推動靠近的 MBON 對該氣味的反應壓低。

## 庫內誰用了它

| 來源 | 記錄的 MBON | 推動靠近或走開（依來源所引） | 怎麼量 | 看到什麼 |
|---|---|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | **未量 MBON** | — | — | 只量 KC 內部；KC→MBON 突觸是否改變，本篇無從回答 |
| [[s-hige-2015-heterosynaptic-plasticity]] | **γ1pedc**（舊名 MB-MVP2，R12G04-LexA 讓它帶綠色螢光蛋白 GFP，方便電極對準）；**α2sc**（R34B02-LexA）；**γ2α′1**（R25D01-LexA） | γ1pedc：靠近（引 Aso 2014b）。α2sc、γ2α′1：該篇未說明，？待查 | 活體全細胞膜片鉗（把玻璃電極接上細胞、直接量細胞內的電訊號）：記錄放電次數（尖峰數）與從突觸流進來的電流（興奮性突觸後電流，EPSC；其累積總量稱電荷，單位 pC） | γ1pedc：氣味配 DAN 一次，突觸長期變弱（長期抑制，LTD）；α2sc：要 1 分鐘的配對才變弱；在 γ1 區配對、讓 γ1 突觸變弱時，鄰區的 γ2α′1 不變 |
| [[s-handler-2019-dopamine-receptor-timing]] | **γ4**（主力；離體 VT026001-Gal4，在體 R53C03-LexA）；**γ2**（25D01-Gal4／25D01-LexA）、**γ5**（66C08-Gal4），兩者在補充圖 S3：？待查 | γ2：靠近；γ4、γ5：走開（皆引 Aso 2014b） | GCaMP6s（[[e-gcamp]]）量區室內樹突的鈣反應 | γ4：多巴胺在後→變弱，多巴胺在前→變強（雙向）；論文說 γ2、γ5 也有類似的雙向改變 |
| [[s-cohn-2015-coordinated-neuromodulation]] | **γ2、γ3、γ4、γ5**（品系名主文未寫） | 該篇未自行檢驗 | γ4 膜片鉗（EPSC）；成對 MBON 的 GCaMP6s；以 P2X2 單獨活化某一顆 MBON | 活體中 γ2/γ3 MBON 對氣味反應遠大於 γ4/γ5，離體時無差別；單獨活化本格 DAN 讓 MBON 增強；**活化任一 γ MBON 都改變各格 DAN** |
| [[s-ichinose-2015-reward-recurrent-circuit]] | **α1**（MB310C、MB323B；兩顆麩胺酸性細胞） | 未量，靠阻斷看記憶 | shibire^ts 阻斷、dTrpA1 活化、RNAi | 訓練與訓練後 1 小時需要它才有 24 小時記憶；活化它可代替糖；末梢緊貼 PAM-α1 樹突 |
| [[s-felsenberg-2017-re-evaluation]] | **V2 群**（MB052B，五型）、**γ2α′1**（MB077C、R25D01-LexA）、**MVP2**（MB112C） | 依延伸圖 1b：PPL1 支配格的 MBON 推動靠近 | 阻斷、離體光遺傳活化、活體 GCaMP | 消退需要 V2、再鞏固需要 γ2α′1；訓練後 γ2α′1 對 CS− 反應變大；阻斷 MVP2 兩者都不受影響 |
| [[s-felsenberg-2018-memory-extinction]] | **MVP2**（γ1pedc>α/β，GABA）、**M4β′**（β′2mp）、**M6**（γ5β′2a）（後兩者麩胺酸） | MVP2 靠近；M4β′、M6 走開（依該篇） | 活體 GCaMP 量樹突與軸突；電顯數突觸 | 消退後 MVP2 的嫌惡痕跡仍在，M6 樹突出現新痕跡；MVP2 → M6 為 16–17 個突觸、→ M4β′ 47 個 |
| [[s-aso-2014-mb-architecture]] | **葉上全部 21 型**（另有非典型的萼部 MBON-calyx，合計 22 型） | 本篇未測行為 | 解剖：對位到標準腦、MCFO 單細胞標記、Syt::smGFP-HA 判極性、抗 dVGluT／GAD1／ChAT 判傳遞物質 | 21 型共 34 顆（每側）；麩胺酸 7 型 8 顆、GABA 4 型 11 顆、乙醯膽鹼 8 型 13 顆、2 型未定；三型把軸突送回葉內，形成前饋網路 |
| [[s-aso-2014-mbon-valence]] | **22 型的篩檢**（31 條 split-GAL4，光遺傳用 25 條、覆蓋 22 型中的 20 型） | **本篇自己測**：25 條中 9 條顯著——走開 3 條全標麩胺酸 MBON，靠近 6 條全標 GABA 或乙醯膽鹼 MBON；16 條不顯著（含 MBON-α1、β2β′2a、β′1） | CsChrimson 光遺傳活化（未訓練、無氣味的四象限場地）；shibire<sup>ts</sup> 阻斷六種記憶作業；dTrpA1 活化看睡眠 | 2 小時嫌惡氣味與嫌惡顏色記憶需要 MBON-γ1pedc>α/β；獎賞記憶需要多型；24 小時長期記憶的讀出需要 V2 群整群；走開型促醒、靠近型促眠；**全篇沒有量任何 MBON 的生理反應** |
| [[s-eschbach-2021-learned-innate-valence-integration]] | **幼蟲**的 24 型 MBON（a1…q1，幼蟲自己的命名，不對應成蟲型別）；功能實驗集中在 MBON-m1（SS02163） | **該篇自己測**：15 個品系涵蓋 18 型——正價值（推動靠近）8 型：a1、b1、b2、d1、e1、g1、g2、m1；負價值（推動走開）6 型：a2、e2、h1、h2、i1、k1；無效果 4 型 | 三齡幼蟲光活化看轉彎與爬行速度；一齡幼蟲鈣成像（GCaMP6f）；電顯追出全部下游 | 負價值 MBON 多住在獎賞記憶的區室、正價值多住在懲罰記憶的區室；價值相反的 MBON 之間有 9 處側向抑制；下游共 167 對；MBON-m1 同時收側角輸入，嫌惡訓練後對 CS+ 的反應約剩三成（※ 從圖判讀） |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | **M4/6 群**（M6 ＝ MBON-γ5β′2a，另含 β′2mp、β2β′2a、β′2mp bilateral；MB011B 或 VT1211-GAL4）；**α′3 的 MBON**（MB027B） | M4/6：高活動把天平推向躲避（該篇圖 9，引 Owald & Waddell 2015）。α′3：該篇未說明，？待查 | 行為（RNAi 後的 T 迷宮與理毛測驗）；GCaMP6f 量樹突與軸突；內生 GFP 標記的受體做 FRAP | 獎賞記憶需要 M4/6 上的 α5（立即）與 α1／α2／Dlg（3 小時），嫌惡記憶不需要；α′3 的熟悉度學習需要 α5 與 α2；重複給同一氣味十次後 α′3 的 MBON 反應降到約 0.07，同格 KC 不變 |
| [[s-yamada-2023-second-order-conditioning]] | **MBON-α1**（麩胺酸性）、**MBON-γ5β′2a**（SS01308） | 依該篇所引，獎賞記憶區室的 MBON 多為麩胺酸性 | 活體全細胞記錄 | 光活化 PAM-α1 配氣味後，MBON-α1 對該氣味的反應下降（補充圖 3-2，本庫未取得）；二階制約後 MBON-γ5β′2a 對 S2+ 的次閾值反應下降。**MBON-α1 是唯一不直接接到其他區室 DAN 的 MBON**（引 Li et al. 2020） |
| [[s-aso-2023-upwind-neurons]] | **未記錄 MBON 本身**：光活化 MBON-α1（MB310C）與 MBON-α3（MB082C；離體鈣成像改用 G0239-GAL4），記錄下游的迎風神經元 UpWiN | 活化篩選中 MBON-γ2α′1（MB077B）與 MBON-γ3／γ3β′1（MB083C）達校正後顯著的迎風；MBON-α3（MB082C）只達未校正的顯著；MBON-α1（MB310C）無效果 | 活體全細胞記錄下游；離體 GCaMP6s；hemibrain 連結體 | MBON-α1（麩胺酸）抑制 UpWiN（17 顆中 4 顆），MBON-α3（乙醯膽鹼）興奮 UpWiN（11 顆中 3 顆）；兩者同時活化時相抵；連結體上 SMP354 收 MBON-α1 268 個、MBON-α3 319 個突觸 |
| [[s-huang-2024-dopamine-memory-dynamics]] | **γ1pedc>α/β、γ2α′1、α2sc、α′2、α3、α′3m** 六型（split-GAL4；阻斷與活化 γ1pedc>α/β 用 MB085C、阻斷 α3 用 MB093C） | 未逐型說明；MBON 對五種氣味都是放電上升，幅度與氣味價值無關（延伸圖 4g） | 頭固定、腳踩小球的活果蠅，電壓成像（pAce）量單次放電；TnT 阻斷、CsChrimson 活化 | 自發約 11–38 次／s（※ 從圖判讀）；電擊訓練後 γ1pedc>α/β、γ2α′1 對 CS+ 下降、約 1 小時恢復，α3 下降持續 24 小時以上；阻斷 α3 → 3 小時記憶消失；γ1pedc>α/β 對 PPL1-α3 的抑制性回饋閘控 α3 的長期改變 |

數字（降幅、n、協定）見 [[numbers]] 與 [[c-kc-mbon-plasticity]]。

※ 推論：Handler 2019 的「γ2 MBON」與 Hige 2015 的 MBON-γ2α′1 可能是同一型細胞。依據是兩篇標記它用的都是 25D01 這段調控序列（Hige：R25D01-LexA；Handler：25D01-Gal4 與 25D01-LexA），而 Felsenberg 2017 延伸圖 6p 明說 R25D01-LexA 標 MBON-γ2α′1。不確定之處：同一段序列做成 GAL4 與 LexA 品系，標到的細胞不一定完全相同，GAL4 版本沒有人比對：？待查（見 [[e-mbon-gamma2alpha1]]）。同理，Handler 的「γ5 MBON」（66C08-Gal4）與 Felsenberg 2018 的 M6（R66C08-GAL4）用同一段序列，※ 推論為同一型（[[e-mbon-gamma5beta2a]]）。

**MBON 不只把結果送出去，也回頭影響 DAN。** Ichinose 2015（α1）、Cohn 2015（γ 葉）、Felsenberg 2017（V2、γ2α′1）、Felsenberg 2018（M4β′／M6 → γ5 PAM）、Huang 2024（γ1pedc>α/β → PPL1-α3 與 PPL1-α′2α2 的抑制）都有這類證據，見 [[t-mbon-dan-feedback]]。

## 已知的問題

- **逆向配對的結果兩篇不同。** Hige 2015 的 γ1pedc：先用光活化 DAN、再給氣味（即多巴胺在前），突觸不變；Handler 2019 的 γ4：多巴胺在前，突觸變強。兩篇的區室、DAN、製備、時間間隔都不同，本頁不裁決，見 [[syn-contradictions]] 1.1。
- **讀出方式不同，數值不能並排。** Hige 用電極量尖峰數與電荷（pC），Handler 用鈣影像的 ΔF/F（螢光相對基線的變化比例）。「降九成」與「ΔF/F 從 1.22 降到 0.42」不是同一種量。Huang 2024 用電壓成像量放電率（次／s），又是第三種量；它對 MBON 的偵測錯誤率最高每秒 1.7 次，對自發只有十幾次的 α′2、α′3m 不可忽略。
- **「推動靠近或走開」多數是引用 Aso 2014b**；Hige 2015、Handler 2019 都沒有自己檢驗所記錄 MBON 的行為效果。**回到 [[s-aso-2014-mbon-valence]] 原文，各型的證據層級並不相同**：單一型別就顯著的只有 MBON-γ4>γ1γ2（MB298B）、MBON-γ1pedc>α/β（只有 MB112C 一條，依該篇方法只算「提示性」）與 MBON-γ2α′1（MB077B、MB090C 兩條）；**γ5β′2a「走開」只有 M4/M6 三型合併（MB011B）的證據**，單標子集的 MB210B、MB002B 不顯著；γ3 與 γ3β′1 沒有品系能分開，只能當一組。引用某一型的方向時要先查它屬於哪一級。
- **「與同區室 DAN 的價值相反」是通則，不是逐格成立。** Aso 2014b 原文寫的是「in general」，而且是**依傳遞物質**分組（麩胺酸＝走開；GABA、乙醯膽鹼＝靠近），不是依 DAN 群（PAM／PPL1）分。原文自己就有反例：γ3、γ3β′1 是 GABA 性 MBON、位在 PAM 支配的範圍，活化後推動靠近；同在 PAM 範圍的 MBON-α1（MB310C）與 MBON-β2β′2a（MB399B）活化後完全沒有偏好（中位數約 0）。所以「PAM 的格裡 MBON 推動走開」不能當成推論某一型方向的依據。
- **「傳遞物質決定推動方向」只在成蟲成立。** 成蟲（Aso 2014b）顯著推動走開的全是麩胺酸性。幼蟲（Eschbach 2021）推動走開的 6 型中有 GABA 性（h1、h2）與乙醯膽鹼性（a2）（※ 依該篇圖 3d 的符號推論，見該來源頁）。引用這條通則時要註明是成蟲。
- **「MBON」的定義是解剖的，不是功能的。** [[s-aso-2014-mb-architecture]] 的定義是「樹突在蕈狀體裡的神經元」，不分傳遞物質，也不管它是不是真的把訊號送出蕈狀體——其中三型的軸突其實送回葉內。另外，短名編到 MBON-22，但「21 型」不含第 22 個（MBON-calyx 樹突在萼部與柄，被歸為非典型），讀到「MBON-22」不要以為有 22 型葉上 MBON。
- **傳遞物質與葉的對應只是趨勢。** Aso 2014a 正文寫「乙醯膽鹼性在垂直葉、麩胺酸性在內側葉、GABA 性在交界」，但同篇表 1 的 MBON-α1、MBON-β1>α 是麩胺酸性而與 α 葉有關，MBON-γ2α′1 是乙醯膽鹼性而樹突有一半在 γ2（⚠️ 單篇自身不一致，見該來源頁第五節）。照字面當分類規則會出錯。
- **「推動靠近或走開」與「推動迎風」是不同的讀數。** Aso 2023：活化 MBON-γ2α′1 讓已經朝上風的果蠅維持朝向，活化 UpWiN 則讓果蠅主動轉往上風；兩者在迎風位移上都顯著，但運動策略不同。同一型 MBON 在二選一偏好上沒有效果（MBON-α1），不表示它對下游沒有作用。
- **有些品系有「第二條品系結果不一致」的前例。** Aso 2014b 表 2 記 MB093C 標 MBON-α3 並弱標 MBON-α′2，而該篇長期記憶（圖 10）與酒精記憶（圖 11）中，MB093C 與另一條 α3 品系 MB082C 的結果不一致，作者推測是非目標表現或遺傳背景不同。Huang 2024 阻斷 MBON-α3 用的正是 MB093C。
- **樹突沒變不等於輸出沒變。** Felsenberg 2018 的 M6：只訓練時樹突的 CS+／CS− 沒差別，軸突卻有；作者以 MVP2 的抑制性輸入落在 M6 樹突根部附近解釋。MBON 之間也互相連結（前饋抑制），一顆 MBON 的輸出可被別格改寫。
- **Huang 2024 的「長期」不是蛋白質合成依賴的長期記憶。** 該篇的「長期」指 MBON-α3 持續 3 到 24 小時的放電改變，沒有用蛋白質合成抑制劑、也沒有測數天的記憶（見 [[c-memory-consolidation]]）。
- **行為由多個區室合成。** Hige 只量 γ1pedc 一個區室就對照整隻果蠅的類化行為（學會躲一種氣味後，也躲相似的氣味）；Handler 也承認行為不只來自 γ4。

## 相關

- 細胞：[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]；結構：[[e-mushroom-body]]
- 各型 MBON：[[e-mbon-gamma1pedc]]、[[e-mbon-gamma2alpha1]]、[[e-mbon-alpha2sc]]、[[e-mbon-gamma4]]、[[e-mbon-gamma5beta2a]]、[[e-mbon-alpha1]]、[[e-mbon-alpha3]]
- 工具：[[e-gcamp]]、[[e-split-gal4]]、[[e-cschrimson]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-mb-compartment]]、[[c-cs-us-timing]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]、[[t-mbon-dan-feedback]]、[[t-memory-updating]]、[[t-mbon-to-action]]、[[t-innate-learned-integration]]；矛盾：[[syn-contradictions]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-eschbach-2021-learned-innate-valence-integration]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-yamada-2023-second-order-conditioning]]、[[s-aso-2023-upwind-neurons]]
