---
title: 蘑菇體輸出神經元（mushroom body output neuron, MBON）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: medium
---

# 蘑菇體輸出神經元（mushroom body output neuron, MBON）

## 是什麼

讀取 [[e-kenyon-cell]]（KC）訊號、再把結果送出 [[e-mushroom-body]] 去影響行為的神經元。每型 MBON 的樹突佔據葉上的一個區室（[[c-mb-compartment]]），在那裡收 KC 軸突送來的訊號；同一區室裡另有一型 [[e-dopaminergic-neuron]]（DAN）調整這個「KC → MBON」突觸的強弱。MBON 以所在區室命名，例如 MBON-γ1pedc 的樹突在 γ1pedc 區室。

**價值（valence）**：直接活化不同的 MBON，會讓果蠅靠近或走開。Hige 2015 與 Handler 2019 都引 Aso et al. 2014b 說明這件事；Hige 2015 另引該文說，一般而言 MBON 推動的行為方向，與同區室 DAN 傳遞的價值相反（例如懲罰 DAN 配推動靠近的 MBON）。而懲罰 DAN 放出的多巴胺，會讓同區室 KC→MBON 的突觸變弱（例：Hige 2015 的 γ1pedc，見下表）。因此學到「這個氣味不好」，就是把推動靠近的 MBON 對該氣味的反應壓低。

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

數字（降幅、n、協定）見 [[numbers]] 與 [[c-kc-mbon-plasticity]]。

※ 推論：Handler 2019 的「γ2 MBON」與 Hige 2015 的 MBON-γ2α′1 可能是同一型細胞。依據是兩篇標記它用的都是 25D01 這段調控序列（Hige：R25D01-LexA；Handler：25D01-Gal4 與 25D01-LexA），而 Felsenberg 2017 延伸圖 6p 明說 R25D01-LexA 標 MBON-γ2α′1。不確定之處：同一段序列做成 GAL4 與 LexA 品系，標到的細胞不一定完全相同，GAL4 版本沒有人比對：？待查（見 [[e-mbon-gamma2alpha1]]）。同理，Handler 的「γ5 MBON」（66C08-Gal4）與 Felsenberg 2018 的 M6（R66C08-GAL4）用同一段序列，※ 推論為同一型（[[e-mbon-gamma5beta2a]]）。

**MBON 不只把結果送出去，也回頭影響 DAN。** Ichinose 2015（α1）、Cohn 2015（γ 葉）、Felsenberg 2017（V2、γ2α′1）、Felsenberg 2018（M4β′／M6 → γ5 PAM）都有這類證據，見 [[t-mbon-dan-feedback]]。

## 已知的問題

- **逆向配對的結果兩篇不同。** Hige 2015 的 γ1pedc：先用光活化 DAN、再給氣味（即多巴胺在前），突觸不變；Handler 2019 的 γ4：多巴胺在前，突觸變強。兩篇的區室、DAN、製備、時間間隔都不同，本頁不裁決，見 [[syn-contradictions]] 1.1。
- **讀出方式不同，數值不能並排。** Hige 用電極量尖峰數與電荷（pC），Handler 用鈣影像的 ΔF/F（螢光相對基線的變化比例）。「降九成」與「ΔF/F 從 1.22 降到 0.42」不是同一種量。
- **「推動靠近或走開」都是引用 Aso 2014b**，兩篇都沒有自己檢驗所記錄 MBON 的行為效果。
- **樹突沒變不等於輸出沒變。** Felsenberg 2018 的 M6：只訓練時樹突的 CS+／CS− 沒差別，軸突卻有；作者以 MVP2 的抑制性輸入落在 M6 樹突根部附近解釋。MBON 之間也互相連結（前饋抑制），一顆 MBON 的輸出可被別格改寫。
- **「推動靠近或走開」各篇的依據不同**：Hige、Handler 引 Aso 2014b；Felsenberg 2017 依自己延伸圖 1b 的通則；都不是該篇自己的行為檢驗。
- **行為由多個區室合成。** Hige 只量 γ1pedc 一個區室就對照整隻果蠅的類化行為（學會躲一種氣味後，也躲相似的氣味）；Handler 也承認行為不只來自 γ4。

## 相關

- 細胞：[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]；結構：[[e-mushroom-body]]
- 各型 MBON：[[e-mbon-gamma1pedc]]、[[e-mbon-gamma2alpha1]]、[[e-mbon-gamma4]]、[[e-mbon-gamma5beta2a]]
- 工具：[[e-gcamp]]、[[e-split-gal4]]、[[e-cschrimson]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-mb-compartment]]、[[c-cs-us-timing]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]、[[t-mbon-dan-feedback]]、[[t-memory-updating]]；矛盾：[[syn-contradictions]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]
