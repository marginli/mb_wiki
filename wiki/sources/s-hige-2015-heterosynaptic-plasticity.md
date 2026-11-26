---
title: "Heterosynaptic Plasticity Underlies Aversive Olfactory Learning in Drosophila"
citation: "Neuron 88(5), 985–998 (2015). doi: 10.1016/j.neuron.2015.11.003 [全文（PMC 免費閱讀）](https://pmc.ncbi.nlm.nih.gov/articles/PMC4674068/)"
created: 2026-10-25
updated: 2026-11-26
tags: [source, active, mb-learning]
confidence: high
---
<!-- 本機 PDF：papers/2015-Heterosynaptic%20Plasticity%20Underlies%20Aversive%20Olfactory%20Learning%20in%20Drosophila.pdf -->

# Heterosynaptic Plasticity Underlies Aversive Olfactory Learning in *Drosophila*

**異突觸可塑性是果蠅嫌惡嗅覺學習的基礎**

| 項目 | 內容 |
|---|---|
| **出處** | Neuron 88(5), 985–998 (2015). doi: 10.1016/j.neuron.2015.11.003 [全文（PMC 免費閱讀）](https://pmc.ncbi.nlm.nih.gov/articles/PMC4674068/) |
| 日期 | 刊期 2015-12-02（PDF 印「Published: December 2, 2015」）；線上先行日 ？待查（PDF 未印）。投稿 2015-05-04・修訂 2015-09-11・接受 2015-10-14 |
| 通訊作者 | Toshihide Hige，higet@janelia.hhmi.org；Glenn C. Turner，turnerg@janelia.hhmi.org（PDF 只有英文名） |
| 作者 | 共 5 人：Toshihide Hige、Yoshinori Aso、Mehrab N. Modi、Gerald M. Rubin、Glenn C. Turner。無共同第一作者標示。分工：Hige 做電生理、Aso 做行為、Modi 做鈣影像 |
| 機構 | Cold Spring Harbor Laboratory（美國紐約州）；Janelia Research Campus, Howard Hughes Medical Institute（美國維吉尼亞州） |
| 資料庫 | 無公開資料庫或程式碼連結（分析以 MATLAB R2014a 自寫程式完成） |
| 補充資料 | Supplemental Experimental Procedures（含行為實驗方法）＋ 圖 S1–S7。**本庫未取得**，本頁凡依賴補充資料的內容一律標 `？待查（補充資料未取得）` |
| 經費 | NIH R01 DC010403-01A1（Turner）；HHMI（Rubin、Aso）；日本學術振興會海外研究員獎助、上原記念生命科學財團（Hige） |

> 與本庫有關的作者：無（本庫目前沒有「與本庫有關的作者」名單）。
>
> 付費期刊（版權屬出版社）。本 PDF 為出版社排版版（Cell Press 版面，頁尾印「©2015 Elsevier Inc.」）；**PDF 內搜尋 Creative Commons／open access／license 皆無結果，沒有 CC 授權聲明**。交辦書目附有 PMC 編號 PMC4674068，該編號未印在 PDF 上。全文請由資料表「出處」列的連結到 PMC 免費閱讀（PMC 公開的作者稿；本庫在本機另存的是出版社排版版）。**本庫不散布全文 PDF。** 本頁的圖擷取自原文，版權屬原出版社，以教學與評論目的引用，每張圖下方標明出處。

---

## 為什麼重要

> 本節假設讀者已略知果蠅嗅覺學習的輪廓。**完全不熟的讀者可以先看「科普文」一節**：那裡有一張白話名詞表，也逐套交代本篇的八套實驗各自怎麼做——Kenyon 細胞、輸出神經元、多巴胺神經元、突觸的送訊號端與收訊號端、蕈狀體的葉分成一格一格的「區室」，都在那裡有白話說明。

**先說一個限制，本篇每一個結論都要放在它裡面讀。** 蕈狀體（mushroom body, MB）是果蠅腦裡一塊把氣味和好壞經驗連起來的構造。本篇把電極接在它的輸出神經元（MB output neuron, MBON，把蕈狀體的訊號送出去的神經元）上，量的是這顆神經元自己放了幾次電，以及有多少電流從突觸（神經元之間傳訊號的接點）流進它。訊號的來源端——Kenyon 細胞（Kenyon cell, KC，蕈狀體裡代表氣味的神經元）的軸突（送出訊號的長纖維）末梢究竟送出了多少——本篇從頭到尾沒有直接量。所以「KC → MBON 的突觸變弱了」不是一個直接讀數，而是由兩件事合起來推出來的：MBON 收到的輸入變少了（圖 3、圖 4），而 KC 這一端看起來沒變（圖 2 以鈣影像量 KC 的細胞體；鈣影像是用會隨細胞內鈣濃度發光的螢光蛋白，間接看神經元的活動，細胞體則是細胞的本體、細胞核所在的那一球。圖 S7 另外量 KC 的興奮性，也就是要注入多少電流才能讓它放電、以及放得多密）。本頁後面幾乎每一處說「這個問題還沒有答案」的地方，都回到這個限制：細胞體與軸突末梢分處細胞的兩端，中間隔著整條軸突，所以圖 2 排除的是「KC 整顆細胞的反應變了」，排除不了「末梢只在 γ1 那一小段局部少送了」（γ1 是蕈狀體裡的一個分區，下一段說明）。

**標準模型，與它一直缺的那一塊。** 果蠅嗅覺學習有一個存在已久的標準模型：氣味由蕈狀體裡的 KC 表徵（哪一小群 KC 放電，就代表哪一個氣味），懲罰或獎賞由多巴胺神經元（dopaminergic neuron, DAN）帶進來，KC 把訊號經突觸送給 MBON，而 DAN 的末梢就伸到這些突觸旁邊。於是**多巴胺應該會改變「KC → MBON」這個突觸的強度**，也就是同樣多的 KC 訊號能讓 MBON 收到多少電流；本篇引言把這個想法歸給 Heisenberg 2003，稱它是果蠅學習的一個重要模型。

模型有解剖學支持。KC 的軸突成束排成幾條「葉」（lobe），依本篇引用的 Aso et al. 2014a（本庫 [[s-aso-2014-mb-architecture]]），各型 MBON 的樹突（收訊號的分枝）沿 KC 軸突鋪成 15 個互不重疊的區室（compartment），而每個區室都有自己的 DAN 把末梢伸進來。**「互不重疊」講的是不同型 MBON 的樹突彼此不重疊，不是說一型 MBON 只能占一格。** 一條 KC 軸突會依序穿過好幾個區室。本篇記錄的那一型 MBON 叫 MBON-γ1pedc，它的樹突同時落在 γ 葉的第 1 格（γ1）與另一塊叫 pedc 的地方，名字因此把兩段併起來寫（依 [[e-mbon-gamma1pedc]]）。**字尾 pedc 是什麼意思，本篇沒有寫出來**（全文搜 pedunculus 沒有結果），本頁也不自行展開；位置上它與 γ1 相鄰，依 [[s-aso-2014-mb-architecture]] 不計在上面那 15 格之內，但有專屬的一型 MBON 與一型 DAN——所以嚴格說，有專屬住戶的分區是那 15 格再加上 pedc 這一塊。這一格的 DAN 叫 PPL1-γ1pedc：後半與 MBON 相同，因為兩者用同一個位置命名；前半的 PPL1 則是依細胞體在腦中的位置分出來的 DAN 群名（依 [[s-aso-2014-mb-architecture]]）。

模型也有行為遺傳學支持：本篇在結果節引 Aso et al. 2010、2014b，把 PPL1-γ1pedc（送多巴胺進來的那一顆）或 MBON-γ1pedc（讀出訊號的那一顆）的突觸輸出關掉，果蠅的嫌惡（aversive，指被電擊這類壞事造成的）嗅覺記憶就受損。

依本篇的說法，在它之前**果蠅身上還沒有人直接量到這個突觸變弱或變強**；本篇在摘要自稱「首次證明」（first demonstration）、在討論自稱「首次刻畫」（first characterization）。先前的證據是鈣影像，而且量的是**軸突**不是細胞體：學習後 KC 軸突的氣味反應變大（本篇引 Akalal 2010、2011、Boto et al. 2014、Tomchik & Davis 2009、Wang 2008、Yu 2006，並加註「but see Zhang & Roman 2013」，沒有說明那一篇哪裡不同）。要注意這一串與本篇不衝突：先前研究量的是軸突、本篇量的是細胞體，而且本篇在 γ1 這一格看到的是 MBON 端下降，不是 KC 端上升。至於 MBON 的反應，先前的鈣影像有的變小、有的變大，方向並不一致。

**本篇直接量到了什麼。** 作者用全細胞膜片鉗（把玻璃電極貼上細胞膜後打穿，直接量這顆細胞的電位或流進它的電流）記錄 MBON，並用光遺傳（讓神經元製造光敏感通道，照光就使它放電）只活化一顆 DAN。一次「正向配對」的內容是：給 1 秒的氣味，從氣味開始後 0.2 秒起打四下各 1 毫秒的紅光（每秒兩下），光代替電擊。（四下光分別落在氣味開始後 0.2、0.7、1.2、1.7 秒，所以**後兩下其實落在氣味關掉之後**，論文正文沒有提這件事；※ 推論，見專業文 3.1 的討論。）就這一次配對，這顆 MBON 對該氣味放出的電由平均 118 次降到 24 次（氣味開始後 1.4 秒內的次數，已扣掉牠沒聞到氣味時本來就有的自發放電；兩個平均值的標準誤各為 ± 8.3 與 ± 7.4，標準誤是平均值可靠程度的指標，量的果蠅越多、彼此越一致就越小；7 隻果蠅的平均，每隻記錄一顆細胞，圖 1F），個別果蠅的降幅平均 80% ± 5.7%，而且在記錄持續的時間裡（至少 40 分鐘）只有少許恢復（圖 S4，本庫未取得）。另一批果蠅改用電壓箝制（由儀器把膜電位固定住，細胞升不到放電所需的電壓）加藥物，讓 MBON 完全不能放電、只量流進來的電流，同一個 1.4 秒窗內累積的電流總量（電荷）降了 90% ± 3.7%（5 隻果蠅，圖 3D）。

**這兩個數字是兩種讀數、兩批果蠅**：放電次數是 MBON 的產出，電荷是它收到的輸入，不是同一個量的兩次測量，「八成」與「九成」不能互相換算。「至少 40 分鐘」是正文描述放電抑制時說的（圖 S4），不是對電荷量的。還有一點論文沒有討論、本頁從圖上讀出來：配對後電流剛開始的峰值只降了一、兩成（※ 從圖判讀），少掉的主要是峰值之後持續的那一段。這兩件事不衝突，因為峰值只占那 1.4 秒最前面的約 0.1–0.2 秒，電荷的絕大部分來自之後的持續段（※ 從圖判讀，見專業文 3.3 與「五、問題與限制」第 8 條）；所以「降九成」指的是整段的總量，不是峰值。

**它同時檢驗了三個長期只有間接證據的假說。** 以下的 p 值是統計檢定的結果，習慣上 p 小於 0.05 才稱「顯著」，p 大於 0.05 表示這批資料測不出差別。

第 1 個，先後順序要不要緊：把順序倒過來（先打四下光，最後一下光之後 0.5 秒才給氣味），MBON 的放電反應沒有變化（7 隻，p > 0.05，圖 1J）。

第 2 個，各區室是不是各自獨立：改用品系 MB099C 活化一組不含 γ1 的 DAN（其中一型把末梢伸進隔壁的 γ2 格），γ1pedc 的 MBON 不變（8 隻，p > 0.05，圖 5D）；反過來，照上面那個正向配對的方式在 γ1 誘發抑制，同時把電極接到隔壁的 MBON-γ2α′1 上（這一型的樹突同時伸進 γ2 與另一條葉上的 α′1 格，名字因此併寫），它也不變（6 隻，p > 0.1，圖 5L）。（MB099C 到底標到哪幾型 DAN，兩份來源說法不同：⚠️ 矛盾｜本篇寫四型 PPL1 DAN、[[s-aso-2016-dan-cell-type-rules]] 寫兩型｜未裁決，見 [[syn-contradictions]] 1.4；兩種說法都不含 PPL1-γ1pedc。）

第 3 個，稀疏編碼（sparse coding，每種氣味只活化一小群 KC）能不能減少記憶互相干擾：這個假說的邏輯是，每種氣味動用的 KC 群越小，不同氣味撞在同一批 KC 上的機會就越低，改寫一種氣味的突觸時波及另一種的機會也越低。本篇發現兩種氣味共用的 KC 越多，配對其中一種時，另一種被連帶抑制得越多（圖 7I：橫軸是某種氣味與被配對那種氣味共同活化的 KC 比例，縱軸是該氣味的放電被抑制的比例，Pearson 相關係數 r = 0.90；r 衡量兩個量是否成比例，範圍 −1 到 1，0.90 算高。8 個資料點指兩次配對實驗各量四種氣味，含被配對的那一種在內——它與自己的重疊定義上就是 1，見專業文 3.7）；行為上，學會躲乙酸戊酯的果蠅也會躲與它共用 KC 的另兩種氣味（圖 7K）。**答案是「能減少，但減不到零」**：氣味之間重疊越少越不互相干擾，而只要有重疊就會波及。要注意這兩半的強度不同：生理上是一條連續的相關，行為上只測了一個方向、而且是另一批果蠅，所以行為那一半能說的是「有類化」（generalization，學會對一種氣味的反應後，對相似氣味也出現同樣反應），不是「越重疊越類化」。

**本庫關心的、還沒有答案的問題。** 一個突觸有兩側：突觸前是 KC 軸突的末梢（送出訊號），突觸後是 MBON（接收訊號）。突觸變弱，可能是末梢送得少，也可能是 MBON 收得少。本篇自己在討論中點出一個未解的落差，牽涉到兩個不同的實驗，先說清楚它們的差別：本篇的主實驗用品系 MB320C，只活化一顆 PPL1-γ1pedc；另外有一組「正對照」用範圍更廣的品系 TH-GAL4（正對照＝一個照理應該出現效果的實驗，用來證明方法本身做得出效果；這一組就是圖 5E–5H），它標到 PPL1 群中的一大部分、含 PPL1-γ1pedc，另外還標少數獎賞群（PAM）的 DAN 與蕈狀體以外的許多 DAN。落差在於：Boto et al. 2014 用的正是 TH-GAL4，他們活化多巴胺神經元後，**在 γ1 這一格的 KC 末梢上**看不到氣味誘發鈣反應的改變（依本頁專業文 3.5，該篇在別的區室有看到 KC 軸突的鈣反應改變，唯獨 γ1 沒有——這也是為什麼上一段那串「KC 軸突反應變大」的引文裡會出現同一篇）；本篇用同一個品系，卻在 MBON-γ1pedc 量到強烈的放電抑制（5 隻，圖 5E–5H）。

為什麼這算對不上：神經元要把訊號送出去，得靠鈣流進末梢，所以末梢如果送得少，一般預期末梢的鈣訊號也會跟著變小。Boto 沒看到鈣訊號改變，本篇卻看到 MBON 端大幅下降，兩者放在一起就湊不攏。作者列出三種可能，沒有裁定：(1) 讓突觸變弱的分子機制位在「鈣流進末梢」這一步的下游，所以鈣照常流進去、送出去的訊號卻變少；(2) 鈣的變化太小、太局部，用散布在整個細胞質裡的鈣指示劑偵測不到；(3) 改變主要發生在突觸後，也就是 MBON 那一側。

**到本庫目前收錄的來源為止，這個問題還沒有答案。** 庫內還有三篇與它直接相關。[[s-tomchik-2009-camp-dynamics]] 量的是突觸**前**端 KC 裡的 cAMP（環腺苷酸，一種細胞內的「第二傳訊者」分子，多巴胺受體被活化後會讓它升高）與鈣，沒有量 KC 送給 MBON 的輸出。[[s-handler-2019-dopamine-receptor-timing]] 處理多巴胺受體與時序規則（氣味與多巴胺相差多久才有效、方向是變強還是變弱），但它量的也是輸出神經元那一側的反應。[[s-pribbenow-2022-postsynaptic-plasticity]] 是庫內第一篇不只「量」突觸後、而是直接**操作**突觸後分子（MBON 上接收 KC 訊號的受體）的——這裡要區分兩件事：本篇與 Handler 2019 都把電極或顯微鏡對著 MBON 量，但沒有動過 MBON 那一側的任何分子，所以不能回答「改變是不是發生在 MBON 身上」。

那為什麼 Pribbenow 2022 也沒有把這個問題關上？因為它動的不是這一格、也不是這種記憶：它降低受體的那群 MBON，樹突在 γ5 與 β′2，另一組熟悉度實驗在 α′3，都不是 γ1；而「同樣的操作對電擊（嫌惡）記憶幾乎沒有影響」本身是一組陰性結果，只能說「在那幾格、對那些受體次單元測不到需求」，不能推論「γ1 的嫌惡可塑性不在突觸後」。庫內把嫌惡學習的突觸改變量得最細的兩篇——本篇的 γ1pedc 與 Handler 2019 的 γ4——都沒有操作過突觸後。**嫌惡學習下突觸前與突觸後的分工，仍然是這條研究線上一個關鍵的未解問題**（整條線見 [[t-dopamine-to-plasticity]]）。
---

## 論文摘要（原文與中譯）

> 本篇的 SUMMARY 是不分段的單段摘要（不是 Background／Results／Conclusion 結構），以下照原文排列。摘要中的「輸出位點」指 KC → MBON 突觸；「突觸抑制」（synaptic depression）指突觸變弱；「長期」在本篇的實測範圍是至少 40 分鐘；「時間先後的邏輯必要條件」指預告用的氣味必須出現在懲罰之前。
>
> Although associative learning has been localized to specific brain areas in many animals, identifying the underlying synaptic processes in vivo has been difficult. Here, we provide the first demonstration of long-term synaptic plasticity at the output site of the *Drosophila* mushroom body. Pairing an odor with activation of specific dopamine neurons induces both learning and odor-specific synaptic depression. The plasticity induction strictly depends on the temporal order of the two stimuli, replicating the logical requirement for associative learning. Furthermore, we reveal that dopamine action is confined to and distinct across different anatomical compartments of the mushroom body lobes. Finally, we find that overlap between sparse representations of different odors defines both stimulus specificity of the plasticity and generalizability of associative memories across odors. Thus, the plasticity we find here not only manifests important features of associative learning but also provides general insights into how a sparse sensory code is read out.

**中譯**（本節為忠實翻譯，非自撰內容）：

> 雖然在許多動物中，聯想學習已被定位到特定腦區，但要在活體內辨識其背後的突觸過程一直很困難。本研究首次證明果蠅蕈狀體的輸出位點存在長期突觸可塑性。將氣味與特定多巴胺神經元的活化配對，會同時引發學習與氣味專一的突觸抑制。可塑性的誘發嚴格取決於兩個刺激的時間先後，重現了聯想學習在邏輯上的必要條件。此外，我們揭示多巴胺的作用侷限於蕈狀體葉的各個解剖區室之內，且在不同區室間有所差異。最後，我們發現不同氣味的稀疏表徵之間的重疊，同時決定了可塑性的刺激專一性，以及聯想記憶在不同氣味之間的可類化程度。因此，我們在此發現的可塑性不僅展現了聯想學習的重要特徵，也為稀疏感覺編碼如何被讀出提供了普遍性的見解。

---

## 科普文

這篇研究的是「嫌惡學習」：果蠅聞到某個氣味時被懲罰，之後就會躲開那個氣味。這是聯想學習（associative learning）的一種：把原本無關的氣味和懲罰聯想在一起。

**要讀懂這篇，先記住一件事：作者的電極只接在「收訊號」的那一顆神經元上。** 他們量的是這一顆收到多少、放了幾次電；「送訊號」的那一端究竟送出了多少，從頭到尾沒有量。所以本篇說的「兩顆神經元之間的接點變弱了」，是由兩件事合起來推的：收訊號的那一顆收得少了，而送訊號的那一群並沒有出現「只跟著配對發生」的改變。後面每一處說本篇「沒有測」「還沒有答案」的地方，都是因為這個限制。

想像一間大公司的收發室。牆上有一長排**投遞口**，每天有一大群**員工**走過去，把信投進投遞口；這一長排投遞口分成幾段，每一段的後面坐著一位**主管**（有的主管同時管相鄰的兩段），讀完信決定公司要「靠近」還是「逃開」。每一件事只由一小群員工負責投信，不同的事由不同的一小群負責，這叫**稀疏編碼**（sparse coding）。收發室裡還有幾位**督察**，每位只管一段投遞口。督察一出聲（代表「剛才發生了壞事」），他那一段裡「剛剛有人投信」的那些投遞口就會被調窄，下次同一批員工投的信，那段後面的主管就收得比較少。這篇論文做的事，就是把電極接在一位主管身上，數他放出多少訊號、又收到多少信。

比喻與真實對象的對照，以及後面會用到的名詞，整理如下。本文從頭到尾用同一組名字，不換詞。

| 比喻 | 真實對象 | 白話解釋 |
|---|---|---|
| 員工 | Kenyon 細胞（Kenyon cell, KC） | 蕈狀體裡數量最多的神經元，一種氣味只讓一小群 KC 發出訊號；哪一小群，就代表哪個氣味 |
| 信 | 神經訊號 | 神經元發出的電脈衝，也叫「放電」 |
| 員工投信的那隻手 | 軸突末梢（突觸前） | 軸突是神經元送出訊號的長纖維；末梢是它的最尾端，緊貼著接點的送訊號側，這一側就叫「突觸前」 |
| 投遞口 | 突觸（synapse） | 兩顆神經元之間傳訊號的接點。本篇關心的是員工送給主管的那些接點 |
| 主管 | 輸出神經元（MB output neuron, MBON）（突觸後） | 收員工的訊號、把結果送出蕈狀體，推動果蠅靠近或走開。接點的收訊號側就叫「突觸後」 |
| 督察 | 多巴胺神經元（dopaminergic neuron, DAN） | 傳遞「剛剛被懲罰」或「剛剛有獎賞」的訊號 |
| 一段投遞口 | 區室（compartment） | 員工的軸突成束排成幾條「葉」（本篇出現 γ、α、α′ 三條；α 與 α′ 是兩條不同的葉，名字只差一撇），每條葉沿長度切成一格一格，一格就是一段。本篇把電極接過三格的主管：γ1（絕大多數實驗）、γ2、α2 |
| 整間收發室 | 蕈狀體（mushroom body, MB） | 果蠅腦中把氣味和好壞經驗連起來的構造 |
| — | 細胞體 | 神經元的本體、細胞核所在的那一球，位在軸突的另一頭，離末梢很遠 |
| — | 製備 | 實驗是在什麼樣的材料上做的：活的果蠅（本篇全部如此）、取出來的腦、還是細胞培養 |
| — | 可塑性（plasticity） | 「接點的強弱會因為經驗而改變」這件事本身 |
| — | CS+／CS− | CS+ 是訓練時與懲罰（本篇以光代替）配在一起的氣味。CS− 是在同一隻果蠅身上另外測的一種氣味，沒有配過懲罰，當作比較基準 |
| — | 正向配對／反向配對 | 正向＝氣味先、督察後（真實世界的順序）；反向＝督察先、氣味後 |
| — | 放電次數 | 每給一次氣味，數牠在氣味開始後 1.4 秒內發出幾次電脈衝，再把多次試驗平均（所以 118 這種數字是「每次氣味的平均次數」，不是多次加總）；已扣掉牠沒聞到氣味時本來就有的自發放電。這是主管的「產出」 |
| — | 突觸電流與電荷 | 電流＝從投遞口流進主管的訊號強度；電荷＝把那 1.4 秒內的電流累加起來的總量，單位皮庫侖（pC）。這是主管的「收入」 |
| — | 電流箝制／電壓箝制 | 全細胞記錄的兩種模式。電流箝制讓電壓自由變化，看得到放電；電壓箝制由儀器把電壓固定住，細胞大致升不到放電所需的電壓，量到的就主要是流進來的電流 |
| — | 品系（driver line） | 一群基因相同的果蠅。基因工程可以讓某個外來蛋白質只在選定的那幾型神經元裡製造出來（行話叫「表現」），不同品系選到的神經元不同 |
| — | 光遺傳 | 讓神經元製造光敏感通道，再用光照使它放電。本篇用的通道叫 CsChrimson，一照紅光就讓神經元放電 |
| — | 鈣影像 | 讓細胞活動時發出較亮的螢光，再用顯微鏡間接看神經元活動。它看的是螢光亮度，不是電 |
| — | 統計顯著 | 統計檢定算出來的 p 值小於 0.05，習慣上才說兩組「差異顯著」；p 大於 0.05 表示這批資料測不出差別，不等於確定沒有差別 |
| — | 標準誤（寫成 ± 幾） | 平均值可靠程度的指標：量的果蠅越多、彼此越一致，這個數字越小。它掛在哪個平均值上，就是那個平均值的標準誤——例如「降幅 90% ± 3.7%」裡，90% 是各隻果蠅降幅的平均，± 3.7% 是這個平均的標準誤 |
| — | 行為分數（PI） | 一群果蠅在兩種氣味之間選擇，換算成一個數；本篇正值表示相對躲開受測的那個氣味 |

**難題**有兩個。第一，要在活的果蠅腦裡把電極接上一顆特定的主管，同時精準控制一位特定的督察何時出聲。依論文自己的說法，在這篇之前，果蠅身上還沒有人直接量到這些投遞口變寬或變窄，缺的就是這種「能只動一位督察」的工具；先前的證據都是間接的（例如用螢光看細胞活動的明暗）。第二，就算看到主管收得變少，也要排除另一種解釋：信是從員工流向主管的，如果員工本身對氣味的反應變弱了，主管收到的自然也會變少，這時改變的就不是投遞口。

**解法**是幾項當時新做的工具。本篇的主角是一位督察 PPL1-γ1pedc 與一位主管 MBON-γ1pedc：名字裡共有的 γ1pedc 指的是位置——牠們同時涵蓋 γ 葉的第 1 格（γ1）與一塊叫 pedc 的地方，所以把兩段併起來寫；**pedc 是什麼意思，本篇沒有寫出來**（全文搜 pedunculus 沒有結果），本文不自行展開。重點是：這位督察管的，正好就是這位主管那一段投遞口。作者新做了一個果蠅品系（名為 MB320C），讓光敏感通道 CsChrimson 只在這位督察身上製造出來——論文的說法是「這個品系只標到一顆 PPL1-γ1pedc 神經元」（這一型每半邊腦只有一到兩顆，依 [[e-ppl1-gamma1pedc]]；左右腦是否各標到一顆，原文沒寫：？待查）。於是作者可以用紅光（波長 627 奈米）代替電擊，時間精確到毫秒。另一套獨立的基因工具讓主管發綠色螢光，方便把玻璃電極接上去。

接下來是本篇的各套實驗。**下面的「第一套、第二套……」是本文為了分清楚而加的編號，論文沒有這樣編**；每一套都註明圖號、用的是什麼製備與記錄模式、量的是什麼讀數、對照組是什麼。**不同套之間經常不能直接比較**，理由在各套之後與最後的「讀數不能互比」一段說明。

**第一套：正向配對（圖 1A–1F）。** 製備是活的果蠅，頭部固定、把腦暴露出來；記錄模式是電流箝制，讀數是主管的放電次數。流程：先記錄兩種氣味（3-辛醇 OCT 與 4-甲基環己醇 MCH）各自讓這位主管放多少電，兩種氣味交替呈現，通常各五次；然後讓其中一種氣味出現 1 秒，並從氣味開始後 0.2 秒起打四下各 1 毫秒的紅光（每秒兩下），這一步叫「配對」；配對後再把兩種氣味各量約五次。與光配對的氣味是 CS+（這一套用 OCT），沒配光的是 CS−（MCH），兩者在同一顆細胞上先後量，CS− 就是這一套的對照。（四下光分別落在氣味開始後 0.2、0.7、1.2、1.7 秒，所以**後兩下其實落在氣味關掉之後**，論文正文沒有提這件事；※ 推論，見專業文 3.1 的討論。）結果（7 隻果蠅，每隻記錄一顆細胞，數字是 7 隻的平均）：CS+ 的放電從每次氣味平均 118 次掉到 24 次，CS− 從 110 次降到 83 次（標準誤分別是 ± 8.3／± 7.4 與 ± 11／± 14）。118 次是在 1.4 秒內，相當於每秒 80 多次——這型神經元本來就放得很密，連沒有氣味時都在放電，上面的數字已經把那部分扣掉了。**兩種氣味都達到統計顯著，但降幅差得很多，而且「配對的效果在兩種氣味之間不同」本身也顯著。** 所以正確的說法是「CS+ 降約八成、CS− 降約四分之一，兩者差異顯著」，不是「只有 CS+ 下降」。抑制在記錄持續的時間裡（至少 40 分鐘）只有少許恢復（這一點畫在補充圖 S4，本庫未取得該圖）。論文另有一組對照果蠅：基因與實驗組相同、只少了讓 CsChrimson 製造出來的那一段，做同樣的氣味配光，反應不變——這說明抑制確實來自光活化督察，而不是光本身或氣味重複呈現（補充圖 S5，本庫未取得該圖）。

**第二套：反向配對（圖 1G–1J）。** 製備、記錄模式、讀數、氣味都和第一套相同，只改順序：先打四下光，最後一下光之後 0.5 秒才給氣味。結果是主管的放電反應沒有變化（7 隻，p > 0.05）。這符合學習的邏輯：預告懲罰的線索要出現在懲罰之前。但要注意本篇只測了這一個反向間隔與第一套那一個正向間隔，**沒有測中間的任何間隔**，也沒有測氣味與光同時開始。

**第三套：檢查員工那一端（圖 2，另加補充圖 S7）。** 製備同樣是活果蠅，但換了儀器與讀數：改用雙光子顯微鏡（一種用紅外線雷射逐點掃描、能看活體深處的螢光顯微鏡）做鈣影像，看的是員工的**細胞體**，讀數是螢光亮度的相對變化，不是電。配對方式與第一套相同，CS+ 一律是 OCT。結果：CS+ 與 CS− 的反應都小幅下降——**而且完全不給光的對照果蠅同樣下降**（那一組兩種氣味都量，合在一起算）。三組（CS+、CS−、不給光）的下降幅度彼此沒有差別，作者把它歸因於成像本身造成的光漂白與光損傷（同一台顯微鏡的雷射反覆照射，使螢光蛋白逐漸變暗），與配對無關。作者還把整群員工的反應樣式當成一個整體來比：哪些員工有反應、各有多強，合起來就是一個樣式，配對前後各量四次，看配對後的樣式離配對前有多遠；結果 CS+ 的樣式並沒有比 CS− 離得更遠。所以這一套要說的不是「員工完全沒變」，而是**「沒有任何只發生在 CS+ 身上的改變」**。另外在補充圖 S7，作者直接用電極記錄 γ 型員工（軸突走 γ 葉的那一類）：因為很難事先找到會對某個氣味反應的員工，他們改用注入電流來模擬氣味反應，配對之後，「要多少電流才開始放電」與「持續給電流時每秒放幾次」都沒有變——這兩項合稱這顆細胞的**興奮性**，也就是它容不容易被激發到放電（該圖本庫未取得，此處只能依正文轉述）。細胞體與注入電流都離 γ1 那一段的投遞口很遠（中間隔著整條軸突），所以這一套排除的是「員工整體變了」，排除不了「員工的手在那一段局部少送了信」。

**第四套：直接量主管的「收入」（圖 3）。** 製備同樣是活果蠅，記錄模式改成電壓箝制，另外在電極內液裡加藥物 QX-314，從細胞內部阻斷放電。兩道手續都要：光靠電壓箝制壓不乾淨（圖 3 的實驗還把仍有放電漏出來的細胞剔除不用），加了藥才能把主管自己的放電完全關掉，量到的就只剩從投遞口流進來的電流。讀數換成電荷。結果（5 隻果蠅）：CS+ 的電荷降了 90%（各隻降幅的平均，標準誤 ± 3.7%），從約 250 降到約 25 皮庫侖（※ 從圖判讀）；CS− 這一次沒有達到顯著（約 275 降到約 220 皮庫侖，※ 從圖判讀）。不過**電流剛開始的峰值只降了一、兩成，少掉的主要是峰值之後持續的那一段**（※ 從圖判讀；論文正文的措辭是電流「在反應早期就大幅降低」，與圖上看到的不完全一致，見專業文 3.3）。這和「總量降九成」不衝突：峰值只占那 1.4 秒最前面的約 0.1–0.2 秒，電荷的絕大部分來自之後的持續段。所以「九成」是整段總量的降幅，不是峰值的降幅。

**第五套：主管自己放不放電有沒有關係（圖 4）。** 第四套已經讓主管完全不能放電卻照樣出現抑制，但它留了一個缺口：第一套看到的是放電次數下降，而第四套根本量不到放電，所以不能排除「主管的放電也參與了那種下降」。這一套補上缺口：**不加 QX-314**，只在配對的那一刻切到電壓箝制壓低主管的放電——因為沒有加藥，壓不乾淨，相對於同一顆細胞配對前的氣味誘發放電壓掉了 83%，還剩約 17%（6 隻果蠅）——配對之後再在電流箝制與電壓箝制之間來回切換，於同一顆細胞上既量放電次數也量電荷。結果兩種讀數都出現和前面相似的抑制（這一套的 CS− 在兩種讀數上也都達到顯著，和第四套不同，⚠️ 論文自身不一致，見專業文 3.4）。嚴格說，這一套證明的是「把放電壓到只剩不到兩成仍然誘發同樣的抑制」，「完全不需要放電」的證據來自第四套，兩套合起來才構成作者的結論：**誘發這個變化不需要主管自己放電**。這一點值得停下來。蝗蟲是另一種昆蟲，別的團隊研究過牠腦中對應構造裡同一類的接點：在那裡，接點會不會改變，取決於收訊號的那一顆有沒有放電、什麼時候放電；果蠅這裡不取決於它，決定因素是「員工在投信的時候督察有沒有出聲」。這種「由第三顆神經元（督察）調整另外兩顆之間的投遞口」的機制，叫做**異突觸可塑性**（heterosynaptic plasticity），也是本篇標題的由來；相對地，只由接點兩端自己的活動決定的改變，叫做同突觸（homosynaptic）可塑性。投遞口變窄並持續，叫做**長期抑制**（long-term depression, LTD）。

**第六套：各段投遞口是不是各自獨立（圖 5）。** 製備與讀數回到第一套（活果蠅、電流箝制、放電次數），改變的是「讓誰出聲」與「記錄誰」，三組的邏輯不同。第一組：改用另一個品系（MB099C）讓一組不包含 γ1 的督察出聲——其中一位管隔壁的 γ2 段——再記錄 γ1 那位主管；換成比喻就是「同一位主管，但出聲的是管隔壁那一段的督察」，結果主管不受影響（8 隻，p > 0.05）。（這個品系標到哪幾型督察，兩份來源說法不同：⚠️ 矛盾｜本篇寫四型 PPL1 多巴胺神經元、[[s-aso-2016-dan-cell-type-rules]] 寫兩型｜未裁決，見 [[syn-contradictions]] 1.4；兩種說法都不含 γ1 這一段的督察，所以不影響這一組的結論。）第二組是正對照——也就是一個照理應該出現效果的實驗，用來證明方法本身做得出效果：改用範圍更廣的品系 TH-GAL4，它標到的督察裡包含 γ1 那一位，結果抑制出現了（5 隻），說明前一組的「沒反應」不是實驗做不出來。第三組反過來：照第一套的方式在 γ1 誘發抑制，但把電極接到隔壁那位主管身上（名字寫成 MBON-γ2α′1，因為牠同時管 γ2 與另一條葉上的 α′1 兩段；誘發抑制的是 γ1，不是牠管的那兩段），牠也不受影響（6 隻，p > 0.1）。第三組並不理所當然：一位員工的軸突會依序經過 γ1、γ2 等好幾段，兩位主管收的大概是同一批員工送來的信，但只有督察管的那一段被調窄。

**第七套：另一段的規則（圖 6）。** 製備、記錄模式與讀數仍是活果蠅、電流箝制、放電次數，記錄的主管換成 α2 這一段的 MBON-α2sc，出聲的督察也換成管那一段的那一位（名叫 PPL1-α′2α2，牠管 α′2 與 α2 兩段，和 γ1 那位是不同型的細胞；本套記錄的是 α2 那一段的主管，α′2 那一段本篇沒有量）。第一套用的 1 秒配對（4 下光）在這裡完全無效（7 隻，p > 0.1）；改用 1 分鐘的氣味配 120 下光，就出現和 γ1 一樣強的抑制（6 隻）。也就是說**不同段對多巴胺的敏感度不同**。兩點保留：這兩個協定同時改了兩件事（氣味長了 60 倍、光多了 30 倍），所以分不出是需要更多多巴胺還是更長的員工活動；而且兩段用的品系不同，兩位督察被光活化的強度不一定相同。順帶一提，γ1 那一段兩種協定都有效（1 分鐘的那組在補充圖 S6A–S6E，本庫未取得該圖），所以差別在 α2 需要更多，不是 γ1 挑協定。

**第八套：重疊、干擾與行為（圖 7）。** 這一套換了氣味組合，也換了光的劑量：四種氣味是乙酸戊酯（PA）、乙酸丁酯（BA）、2-庚酮（HP）、乳酸乙酯（EL）；前三種活化的員工高度重疊，EL 則很不一樣（重疊程度取自同一團隊 Campbell et al. 2013 的資料）。要注意「很不一樣」是相對於 PA、BA、HP 三者之間的高度重疊而言，不是「完全不重疊」——圖 7I 八個資料點中重疊最低的那一個也還有約一成（※ 從圖判讀，見專業文 3.7）。配對改成只打一下 1 毫秒的光，比第一套溫和。生理部分（活果蠅、電流箝制、放電次數）：拿 PA 配對，PA、BA、HP 的反應都顯著下降，EL 不受影響（7 隻），而且 PA 自己的降幅只略強於 BA 與 HP；反過來拿 EL 配對，EL 的下降最強、HP 也顯著下降，PA 與 BA 不顯著（5 隻）。HP 會被 EL 波及，與「重疊決定波及」這個框架相容，因為 EL 與 HP 並非完全不重疊；但**為什麼偏偏是 HP 而不是 PA、BA，本篇沒有回答**——論文正文只說拿 EL 配對時另外三種氣味「變化很小」，也沒有在正文列出 EL 與各氣味各自的重疊比例，只能從圖 7I 的橫軸讀（見專業文 3.7）。把「某種氣味與配對氣味共用的員工比例」對「那種氣味被抑制的比例」畫圖，八個資料點（兩次配對實驗各量四種氣味）的相關係數是 0.90（相關係數衡量兩個量是否成比例，範圍 −1 到 1，0.90 算高）。行為部分**是另一批果蠅、另一套刺激**：用紅光代替電擊訓練，測驗時讓果蠅在 PA、BA 或 HP 與 EL 之間二選一，結果學會躲 PA 的果蠅也會躲另外兩種與牠重疊高的氣味（行為分數約 PA 67、BA 42、HP 38，不配對的對照組約 5、9、−2，※ 從圖判讀；每組 n = 10，正文與圖說都沒有寫明這是 10 隻果蠅還是 10 群果蠅，分數的計算公式也只寫在本庫未取得的補充資料裡，所以 67 對應多強的迴避無法換算：？待查。能比的是配對組明顯高於不配對的對照組）。**作者的結論是：記憶會「類化」（generalization，學到一件事後對相似的東西也有同樣反應）到別的氣味，是因為它們共用了同一批被調窄的投遞口。** 這是兩組結果的對應，不是在同一隻果蠅上證明的因果——作者沒有做「擋住 γ1 的抑制，類化就消失」這種實驗。

**讀數不能互比，這是看這八套實驗時最容易出錯的地方。** 第一、二、五、六、七、八套量的是放電次數（主管的產出），第四、五套量的是突觸電流與電荷（主管的收入），第三套量的是螢光亮度（而且看的是員工的細胞體），第八套的後半量的是一群果蠅的行為分數。單位不同、量的位置不同、甚至果蠅都不同，所以「放電降八成」與「電荷降九成」不是同一個量的兩次測量，「行為類化」與「生理被波及」也只能各自換算成相對比例之後才好並排看（見專業文 3.7）。另外，第八套的光劑量比第一套低，抑制幅度本來就不該直接和第一套比。

回到收發室的比喻。督察調整的是「剛剛有人投信」的投遞口。如果兩件事由完全不同的員工負責，調整一件事的投遞口不會影響另一件。如果兩件事有三成員工重疊，調整其中一件時，那三成共用的投遞口也被調窄了，另一件就會跟著受影響。可以粗略估算：第一套裡配對氣味（OCT）的放電少了約八成；沒配對的 MCH 只有三成的信經過這些被調窄的投遞口，所以它應該少掉約 0.33 × 0.8 ≈ 四分之一。第一套的實測正是如此：MCH 從 110 次降到 83 次，正好約四分之一。（※ 推論：這個估算是本文拿論文的數字算的，論文沒有這樣算，而且假設每位員工的份量相同、抑制是線性的。論文給了兩個重疊比例——「對 MCH 有反應的員工裡有 33% 也對 OCT 有反應」與「對 OCT 有反應的員工裡有 30% 也對 MCH 有反應」，兩者的分母不同；這裡被波及的是 MCH，所以要用的是 33% 那一個。論文沒有說這兩個數字是從哪一批資料算出來的，本頁推測來自第三套那批細胞，見專業文 3.2。）稀疏編碼的好處，就是讓這種「誤傷」降到最低；但只要有重疊，誤傷就不會是零，而行為上的類化正是這種誤傷的另一面。

這個結果和主管的角色也對得上。依本篇引用的 Aso et al. 2014b，用光活化 MBON-γ1pedc 會讓果蠅靠近，也就是這位主管的活動在推動「靠近」。果蠅學會躲某個氣味之後，這個推動靠近的訊號對該氣味就應該變弱——本篇量到的正是這個方向。要說清楚這一步在比對什麼：被接上電極的那些果蠅並沒有測行為，所以這是把本篇的生理方向與另一篇論文的行為方向對起來，不是在同一隻果蠅身上證明的因果；而且這一步成不成立，取決於 Aso et al. 2014b 把這位主管歸在「活化會讓果蠅靠近」那一類是否正確，本篇沒有自己檢驗過。

**代價與限制**也要說清楚。這是在頭部被固定、腦部暴露的活果蠅身上做的，主要協定只配對一次，量的時間跨幾十分鐘；它不是在量果蠅隔天還記不記得。行為實驗與電極記錄是兩批不同的果蠅、兩套不同的光刺激，所以「投遞口變窄造成行為改變」是兩組結果的對應。順序的實驗只有正向與反向各一個間隔。全篇只看到投遞口變窄，沒有看到變寬；但本篇讓出聲的主要是傳遞懲罰的那一群督察（這一群叫 PPL1，是依細胞體在腦中的位置分的，督察名字前半的 PPL1 就是它；第六套的 TH-GAL4 那一組另含少數獎賞群的督察），負責獎賞的督察會在牠們自己那一段造成什麼方向的改變，本篇沒有測。

**最容易被誤讀的一點：這篇說的是「多巴胺讓輸出端的投遞口變窄」，而不是「記憶就存在員工裡」。** 把改變定位到「員工與主管之間的投遞口」，作者靠的是兩件事：流進主管的電流降了九成，而依論文的說法，員工送來的信「照理是這位主管最主要的輸入」（第四套）；以及員工整體的反應與興奮性都沒有只發生在 CS+ 身上的改變（第三套）。（※ 推論：還可以加上第六套第三組——同一批員工的軸突通往隔壁那一段的主管卻完全不受影響；如果改變出在員工整體或更上游，隔壁那位主管也該跟著變。論文沒有把這一組當成定位的依據，只用它論證各段獨立。）作者自己對第一件事留了一個保留：除了員工之外，還有別的神經元把訊號送進這位主管，它們也可能有貢獻。

**但投遞口的哪一側變了，本篇沒有回答。** 作者看的是員工的細胞體與整顆細胞的興奮性，員工的手（軸突末梢）有沒有局部改變，本篇沒有直接量。這裡有一個作者自己寫進討論的麻煩：另一篇研究用第六套第二組那個品系（TH-GAL4）活化督察之後，在 γ1 那一段的員工的手上看不到鈣訊號的變化。照「送得少就該看到活動變小」的道理，這應該指向「改變在主管那一側」；但作者沒有這樣下結論，而是列了三種可能都沒有裁定（機制在鈣流進末梢之後的步驟、鈣的變化太小測不到、改變主要在主管那一側），所以這件事既沒有證實突觸前、也沒有證實突觸後。究竟是員工的手送得少（突觸前），還是主管收得少（突觸後），仍然是開放的問題。
---

## 專業文

### 一、概述

**主要問題。** 果蠅 MB 的 KC → MBON 突觸，是否真的會因為氣味（CS，條件刺激，conditioned stimulus）與多巴胺（US，非條件刺激，unconditioned stimulus 的替代）配對而改變強度？若會，它的誘發規則是否具備聯想學習所需的性質：時間先後、區室專一、刺激專一？

**重要性。** 這是 MB 學習模型的核心假設。Heisenberg 2003 提出「DAN 在各區室異突觸地調節 KC 輸出突觸」的模型；Aso et al. 2014a 的解剖圖譜顯示 15 個區室各有對應的 DAN 與 MBON；Aso et al. 2014b（本庫 [[s-aso-2014-mbon-valence]]）與 Owald et al. 2015 顯示活化不同 MBON 會引發趨近或迴避，也就是 MBON 帶有「正負價值」（valence）。這些都是間接證據。**作者在摘要中自稱「首次證明」（first demonstration）MB 輸出端的長期突觸可塑性**；本庫沒有收錄 Heisenberg 2003 等被引的那幾篇，所以無從獨立驗證這個優先權宣稱。

**發表當時的領域現狀（2015）。** 蝗蟲（Cassenaer & Laurent 2007、2012）與蜜蜂（Oleskevich et al. 1997）已在 MB 輸出端以電刺激誘發可塑性，蝗蟲的形式是依賴突觸後放電的 Hebbian 尖峰時序依賴可塑性（spike-timing-dependent plasticity, STDP）。果蠅方面只有鈣影像：KC 軸突在學習後反應增加（Akalal et al. 2010、2011；Boto et al. 2014〔該篇在部分區室看到 KC 軸突鈣反應改變，但在 γ1 區沒有，見 3.5〕；Tomchik & Davis 2009；Wang et al. 2008；Yu et al. 2006；但 Zhang & Roman 2013 不同），MBON 有的減少（Owald et al. 2015；Séjourné et al. 2011）、有的增加（Bouzaiane et al. 2015；Owald et al. 2015；Pai et al. 2013；Plaçais et al. 2013）。DAN 受器方面，Kim et al. 2007 與 Qin et al. 2012 顯示 KC 上的多巴胺受器是學習所必需。同一團隊在本篇之前（Hige et al. 2015, *Nature*）已報告 MBON 的氣味反應在個體之間差異很大，推測是經驗塑造的結果。

**體裁：** 原著論文（活體電生理 ＋ 雙光子鈣影像 ＋ 行為）。

**讀專業文前的術語與標記**（後文首次出現時不再重複解釋）：

| 詞 | 意思 |
|---|---|
| KC、MBON、DAN | Kenyon 細胞（KC）是 MB 的主體神經元，負責表徵氣味；MB 輸出神經元（MBON）接收 KC 的訊號、影響行為；多巴胺神經元（DAN）傳遞懲罰或獎賞訊號。訊號方向是 KC → MBON，DAN 在旁邊調節這個突觸 |
| 異突觸可塑性、LTD | 由第三個神經元（此處為 DAN）改變另外兩者（KC → MBON）之間突觸強度的現象，稱異突觸（heterosynaptic）可塑性；只由突觸兩端自身活動決定的，稱同突觸可塑性。突觸變弱並持續一段時間，稱長期抑制（long-term depression, LTD） |
| 稀疏編碼 | 每種氣味只活化一小部分 KC；不同氣味用到的 KC 重疊越少，改動一種氣味的突觸越不會波及另一種（這種波及稱「突觸干擾」） |
| OCT、MCH 等氣味 | OCT＝3-辛醇、MCH＝4-甲基環己醇（圖 1–6 用的一對氣味）；PA＝乙酸戊酯、BA＝乙酸丁酯、HP＝2-庚酮、EL＝乳酸乙酯（圖 7） |
| 驅動品系（driver） | 決定某個基因（例如光敏感通道）只在哪些神經元表現的果蠅品系，例如 MB320C、MB099C、TH-GAL4；原理見「二、方法」的遺傳工具段 |
| 光遺傳、熱遺傳 | 光遺傳：讓神經元表現光敏感通道，以光照使其放電（本篇用紅光與 CsChrimson）。熱遺傳：讓神經元表現溫度敏感通道，以升溫使其放電（只出現在引用的 Boto 2014） |
| CS+／CS− | CS＝條件刺激（conditioned stimulus），本篇是氣味。CS+ 是與多巴胺活化配對的氣味，CS− 是不配對、當作對照的另一種氣味 |
| US | 非條件刺激（unconditioned stimulus），原本是電擊；本篇以光活化 DAN 取代，稱「US 替代」 |
| 葉、區室 | KC 軸突成束形成 α、β、α′、β′、γ 等「葉」；葉沿長度分成 15 個區室；本篇只說各區室「互不重疊」、而且不同型 MBON 的樹突與**不同**型 DAN 的軸突重疊（PDF 第 986 頁），**沒有說一型對一型**。依本庫 [[s-aso-2014-mb-architecture]]，實際是 21 型 MBON 與 20 型 DAN 分布在 15 格（13 型 MBON 只進一格、8 型進兩格），另有 pedc 不計在 15 格內但有專屬住戶。本頁先前寫「每區室有一型 DAN 與一型 MBON」，已更正。一條 KC 軸突依序穿過多個區室，沿途與各區室的 MBON 形成突觸 |
| PPL1、PAM | 兩群多巴胺神經元的名稱。本篇只說 PPL1-γ1pedc 的活化可取代嫌惡的電擊；PAM 只在 TH-GAL4 的圖說中出現，本篇未說明其功能 |
| 價值（valence） | MBON 被活化時引發的是趨近（正價值）或迴避（負價值） |
| 尖峰（spike） | 神經元的動作電位，即「放電」；本篇以氣味開始後 0–1.4 s 內的尖峰數當作 MBON 的反應量 |
| EPSC、電荷轉移 | EPSC 是興奮性突觸後電流（從突觸流進 MBON 的電流）；電荷轉移是 EPSC 在 0–1.4 s 內的時間積分，單位 pC（皮庫侖），代表整段反應收到的突觸輸入總量，不同於電流的峰值 |
| QX-314 | 放進記錄電極內液、從細胞內部阻斷鈉通道的藥物，使被記錄的 MBON 無法放電 |
| 第二傳訊者 | 受器被活化後在細胞內傳遞訊號的小分子，cAMP 是其一；它能在細胞內擴散，所以有可能沿 KC 軸突跑到鄰近區室 |
| Hebbian STDP | 尖峰時序依賴可塑性（spike-timing-dependent plasticity）：突觸強度的改變取決於突觸前、後兩個神經元放電的先後，需要突觸後神經元放電；「Hebbian」指這種由兩端共同活動決定的規則 |
| DPM 神經元 | 廣泛支配 MB 各葉的一種神經元（dorsal paired medial），也可能把訊號送到 MBON 附近 |
| 電流箝制、電壓箝制 | 全細胞記錄的兩種模式。電流箝制讓膜電位自由變化，可看到尖峰；電壓箝制由儀器把膜電位固定在設定值，細胞無法升到放電所需的電位，所以尖峰大多被壓掉，此時量到的是流入細胞的電流 |
| PSTH | 刺激前後的平均放電率時間曲線（peristimulus time histogram） |
| ΔF/F、GCaMP6f | GCaMP6f 是鈣指示蛋白，神經元活動時細胞內鈣升高、螢光變亮；ΔF/F 是螢光相對基線的變化比例，作為活動量 |
| 類化（generalization） | 學會對一種氣味的反應後，對相似氣味也出現同樣反應 |
| 重複量測雙因子 ANOVA | 本篇的兩個因子是「配對前／後」與「氣味（CS+／CS−）」，同一隻果蠅前後都量；「配對效果在兩種氣味間顯著不同」指兩因子的交互作用顯著 |
| ※ 推論 | 論文沒有明說、本頁自行推得的內容 |
| ※ 從圖判讀 | 本頁從圖上的長條或曲線估讀的數值，論文沒有明列 |
| ？待查 | 需要補充資料或其他來源才能確認、本頁刻意不填的內容。本篇的補充資料（圖 S1–S7）未取得，所以凡是只寫在補充資料裡的細節都標此記號 |
| 本頁、本庫 | 本頁＝這份閱讀筆記；本庫＝收錄這份筆記的果蠅學習與記憶文獻知識庫（目前收錄 28 篇論文） |


### 二、方法

```mermaid
flowchart TD
    A["遺傳設計<br/>split-GAL4 → CsChrimson（只在特定 DAN）<br/>LexA → GFP（標 MBON 供電極定位）或 GCaMP6f（KC）"] --> B["雜交第一代（F1）雌蠅，羽化（蛹變為成蟲）當天收集<br/>全反式視黃醛 0.5 mM，暗處 36–72 h"]
    B --> C["活體製備，頭部固定<br/>全細胞記錄 MBON（電極 5–7 MΩ；<br/>電壓箝制用的銫內液為 3–5 MΩ）<br/>或雙光子影像 KC 細胞體（920 nm，20× NA 1.0）"]
    C --> D["配對前基線<br/>1 s 氣味，間隔 25 s，兩種氣味交替<br/>通常 5 次（3–10 次）"]
    D --> E["一次配對（基線後 1 min）<br/>CS+ 1 s ＋ 627 nm 紅光 14.7 mW/mm²<br/>1 ms × 4 @ 2 Hz，起於 CS+ 開始後 0.2 s"]
    E --> F["配對後 1 min 給 CS−（無光）"]
    F --> G["再 1–1.5 min 後量配對後反應<br/>每種氣味通常 5 次（至少 3 次）"]
    G --> H["分析：0–1.4 s 視窗內尖峰數（扣除自發放電）<br/>EPSC 電荷轉移（pC）<br/>重複量測雙因子 ANOVA ＋ Tukey 事後檢定"]
    E -.-> V["協定變體<br/>反向：光在前，末次光後 0.5 s 給氣味<br/>1 min：60 s 氣味 ＋ 120 脈衝 @ 2 Hz<br/>單脈衝：1 ms × 1，於 CS+ 開始後 0.8 s"]
    I["行為（另一批果蠅）<br/>光遺傳取代電擊；乙酸戊酯（PA）配對或不配對<br/>測驗：PA、乙酸丁酯（BA）或 2-庚酮（HP）三者之一<br/>對乳酸乙酯（EL）二選一，n = 10／組"]
```

**遺傳工具。** 這篇的核心是精準度。GAL4 是一種能開啟目標基因的蛋白（轉錄因子），在哪些細胞裡製造它，取決於接在它前面的調控序列（啟動子）。split-GAL4 把 GAL4 拆成兩半，各由一段不同的啟動子控制；只有在兩段啟動子都開啟的細胞裡，兩半才會湊成完整的 GAL4。這樣能把表現範圍縮到少數幾型、甚至一顆神經元。作者新做了兩個品系：**MB320C** 只標一顆 PPL1-γ1pedc（PPL1 是多巴胺神經元的一個細胞群名稱，γ1pedc 指它投射的區室；舊名 MB-MP1）；**MB099C** 標四型 PPL1 DAN（PPL1-γ2α′1、α′2α2、α′3、α3），但從不標 PPL1-γ1pedc。GAL4 已經用來在 DAN 裡放光敏感通道，所以要標記被記錄的 MBON 時，需要另一套互不干擾的表現系統，即 LexA。它用來把 GFP（綠色螢光蛋白，讓電極能對準目標細胞）放在要記錄的 MBON 上，或把鈣指示劑 GCaMP6f 放在全部 KC 上（R13F02-LexA）。MBON 的 LexA 品系：R12G04（MBON-γ1pedc，舊名 MB-MVP2）、R25D01（MBON-γ2α′1）、R34B02（MBON-α2sc）、R14H06（γ KC）。

**一個值得記下的設計選擇。** 先前文獻中 PPL1-γ1pedc 的專一品系是 MB438B，作者不用它，因為它的插入位點 attP40 與這裡用的 LexA 品系相同，可能發生 transvection（同源染色體上相同位點的調控元件互相影響），讓 LexA 與 GAL4 在同一批細胞表現（Mellert & Truman 2012）。後果會是光敏感通道也出現在被記錄的 MBON 上，光照就會直接讓 MBON 本身受影響。這是一個實作上的細節，但說明作者在意「光到底活化了誰」。

**光遺傳。** CsChrimson 是紅光活化的陽離子通道，需要飼料中加視黃醛（retinal）作為輔因子。光源為 627 nm LED，強度 14.7 mW/mm²。作者在補充圖 S2 確認光脈衝能在 PPL1-γ1pedc 與 PPL1-α′2α2 引發可靠的尖峰；各品系的表現圖在圖 S1。**兩者細節皆 ？待查（補充資料未取得）**；本頁因此只能依正文的轉述，相信光脈衝確實讓目標 DAN 放電。

**電生理。** 全細胞膜片鉗（whole-cell patch clamp）：把玻璃電極貼上細胞膜後打穿，直接量細胞內電位（電流箝制，current clamp，看尖峰）或流入的電流（電壓箝制，voltage clamp，看興奮性突觸後電流 EPSC）。電流箝制時以 < 50 pA 超極化電流把細胞維持在約 −60 mV。電壓箝制用含銫的內液並加 **QX-314**（10 mM），這是從細胞內阻斷鈉通道的藥物，可完全消除 MBON 自己的尖峰；電極 3–5 MΩ，串聯電阻 < 15 MΩ、補償至多 80%，維持於 −70 或 −60 mV，有未箝住尖峰的細胞剔除；訊號 5 kHz 低通、10 kHz 取樣。部分實驗以 cell-attached 記錄（不打穿細胞膜，只量尖峰）代替；作者說兩種記錄方式量到的尖峰效果無法區分，因此合併呈現。各圖所含例數：圖 1E–F、1I–J、7D–E 各 1 例，7G–H 2 例，S3 1 例。MBON-γ2α′1 的細胞體在**嗅葉**腹側（原文 ventral to the antennal lobes），記錄時需把頭在頸部轉 180°。

**氣味。** 40 ml 瓶裝 5 ml 純氣味，頂空蒸氣經兩段空氣稀釋至 2%（類化實驗為 1%），總流量 1 l/min，以光離子化偵測器（PID）監測穩定性。氣味：3-辛醇（OCT）、4-甲基環己醇（MCH）、乙酸戊酯（PA）、乙酸丁酯（BA）、2-庚酮（HP）、乳酸乙酯（EL）。

**鈣影像。** 雙光子顯微鏡，920 nm，樣本處 8–14 mW，20× NA 1.0 物鏡；影像 255 × 256 像素，像素停留時間 1.6 µs，平均 4.8 Hz。每種氣味配對前後各 4 次（每次 21 s），間隔約 40 s；配對方式同電生理，CS+ 一律為 OCT、CS− 為 MCH（電生理則有一組實驗把兩者對調，見圖 S3）。KC 細胞體逐顆手動圈選（每隻 82 ± 9 顆，mean ± SD，n = 7 隻）。某顆細胞在某次試驗「有反應」的定義：反應視窗（刺激後 0.5–4.5 s）經五格移動平均後的 ΔF/F 峰值超過基線（刺激前 5 s）的 2.33 個標準差；至少半數試驗過閾值才算該氣味的反應細胞。族群分析把一次試驗視為「每顆細胞一個維度」空間中的一點，問的是「配對後的族群反應樣式，有沒有離開配對前的位置」：先求配對前各次試驗的平均點（重心），再算配對後每次試驗到這個重心的歐氏距離；為了讓不同果蠅可比，距離除以重心到原點的距離。若 CS+ 的距離明顯大於 CS−，就表示配對專門改變了 CS+ 的 KC 反應樣式；主成分分析的前兩個成分分別解釋 54% 與 22% 變異。

**資料分析。** MATLAB R2014a。尖峰以高通濾波後依振幅自動偵測並目視確認；PSTH（peristimulus time histogram，刺激前後放電率時間圖）以 SD 50 ms 的高斯核平滑。KC 興奮性測試（圖 S7，目的是排除「配對讓 KC 本身變得較不容易放電」）：以 20 pA/s 斜坡電流找尖峰閾值（膜電位變化率首次超過 3 V/s 處），以 15 pA、1 s 方波（約平均閾值電流的 1.5 倍）量持續放電率。

**行為。** 光遺傳取代電擊作為 US，在嗅覺競技場中訓練（圖 S1C–H），方法在補充實驗程序中。**行為實驗的光強、詳細流程與學習表現指數（performance index, PI；正值表示迴避受測氣味）的計算公式 ？待查（補充資料未取得）。** 從圖 7J 可讀出的部分：配對組在約 2–3 min 給 PA 並同時打 500 ms × 12 的光脈衝，不配對組在 0–1 min 給光、2–3 min 才給 PA（光與氣味錯開，學不到兩者的關聯，作為對照），兩組都在約 4–5 min 測試。行為組飼育條件：22 °C、相對濕度 60%、全暗；視黃醛羽化前 0.2 mM、羽化後 0.4 mM。

### 三、結果

#### 3.1 一次配對引發長效、氣味專一的抑制（圖 1）

![Figure 1：正向配對氣味與 DAN 活化，在 γ1 區室引發長效抑制](../../assets/hige2015-fig1.jpg)

<small>圖片出處：Hige T, Aso Y, Modi MN, Rubin GM, Turner GC. *Neuron* 88(5):985–998 (2015)，Figure 1。© 2015 Elsevier Inc. 教學引用；全文見 [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4674068/)。</small>

> **原圖說（Figure 1）：** Forward Pairing of Odor and DAN Activation Induces Long-Lasting Suppression in the γ1 Compartment. (A) Schematic of MB lobes showing DAN-MBON compartments. (B) Expression of CsChrimson and GFP was driven by MB320C and R12G04-LexA, respectively. Recordings were made from MBON-γ1pedc. (C) Forward pairing protocol. Four light pulses (1 ms in duration) were delivered at 2 Hz, starting 0.2 s after CS+ onset. (D) Representative single-cell data, showing odor responses before (Pre) and after (Post) pairing. Gray bar, 1 s odor presentation. Scale bar, 20 mV. Raster plots (bottom) show spikes. (E) Mean spike rates over several experiments displayed as peristimulus time histogram (PSTH; ±SEM, shaded area; n = 7). (F) Mean odor-evoked spike count (±SEM). Gray lines indicate data from individual flies. Spike counts decreased in both CS+ (OCT, p < 10⁻⁴, Tukey's post hoc test) and CS− (MCH, p < 0.01), but the effect of pairing was significantly different between odors (p < 0.001, repeated-measures two-way ANOVA). (G) Backward pairing protocol. Odor was delivered 0.5 s after the last pulse of light. (H) Representative single-cell data. (I) Mean PSTH (n = 7). (J) Mean odor-evoked spike count. Backward pairing showed no effect (p > 0.05, repeated-measures two-way ANOVA).

**圖說中譯：** 正向配對氣味與 DAN 活化，在 γ1 區室引發長效抑制。(A) MB 葉的示意圖，標出 DAN–MBON 區室。(B) 以 MB320C 驅動 CsChrimson、R12G04-LexA 驅動 GFP；記錄 MBON-γ1pedc。(C) 正向配對協定：四個 1 ms 光脈衝，2 Hz，於 CS+ 開始後 0.2 s 起始。(D) 單一細胞代表資料，配對前（Pre）與配對後（Post）的氣味反應；灰條為 1 s 氣味；比例尺 20 mV；下方光柵圖為尖峰。(E) 多次實驗的平均放電率 PSTH（±SEM，陰影；n = 7）。(F) 平均氣味誘發尖峰數（±SEM）；灰線為個別果蠅。CS+（OCT，p < 10⁻⁴，Tukey 事後檢定）與 CS−（MCH，p < 0.01）的尖峰數都下降，但配對的效果在兩種氣味間顯著不同（p < 0.001，重複量測雙因子 ANOVA）。(G) 反向配對協定：最後一個光脈衝後 0.5 s 才給氣味。(H) 單一細胞代表資料。(I) 平均 PSTH（n = 7）。(J) 平均氣味誘發尖峰數；反向配對無效果（p > 0.05，重複量測雙因子 ANOVA）。

**解讀：**

- **CS− 也顯著下降，正文前後說法不一。** 正文在描述本圖時說 MCH「minimally affected」（110 ± 11 → 83 ± 14），圖說卻寫 p < 0.01；以平均值算是 −25%，後文（第 990 頁）引為 27% ± 7.1%，並改口「slightly, but significantly」。⚠️ 論文自身不一致（措辭層級，不涉及數值）。**真正的結論應寫成「CS+ 降約八成、CS− 降約四分之一，兩者差異顯著」，而不是「只有 CS+ 下降」。**（八成：正文明列 CS+ 由 118 ± 8.3 降到 24 ± 7.4，個別果蠅降幅平均 80% ± 5.7%。）
- **拿論文的數字算它沒算的量：CS− 的抑制幅度約等於「重疊比例 × CS+ 抑制幅度」。** 論文在第 992 頁給出 OCT 與 MCH 的 KC 重疊：MCH 反應細胞中 33%、OCT 反應細胞中 30% 對兩者都反應。邏輯是：配對只削弱「CS+ 活化的那批 KC」通往 MBON 的突觸；CS− 若有一部分 KC 與 CS+ 共用，這部分的輸入也會被一起削弱。若 MBON 對某氣味的輸入大致與活化的 KC 數成正比，而重疊的那批 KC 突觸被抑制了約 80–90%，則 CS− 預期下降 0.30–0.33 × 0.80–0.90 ≈ 24–30%，與實測 27% 吻合。※ 推論：這個算式假設每顆 KC 對 MBON 的權重相同、抑制是線性的，論文沒有做這個計算；作者的定性說法（「may reflect a small degree of overlap」）與它方向一致。
- **正向協定有一半的光落在氣味結束之後。** 四個脈衝在 CS+ 開始後 0.2、0.7、1.2、1.7 s，而氣味只有 1 s，所以後兩個脈衝在氣味關掉後 0.2 與 0.7 s。C 格的示意圖畫得出來（兩條紅線在方波外），正文沒有提。這表示「正向」其實包含部分「痕跡配對」（trace pairing，CS 結束後才給 US）。不過 KC 的反應會持續到氣味結束後一段時間（圖 2A–D 的鈣訊號持續數秒），所以後兩下光到達時，CS+ 活化的 KC 很可能仍在活動，「KC 活動與多巴胺同時出現」的條件仍成立，這不推翻結論。※ 推論。
- **時間規則只有兩個點。** 正向（第一下光在氣味開始後 0.2 s）有效、反向（四下光在 2 Hz 下跨 1.5 s，最後一下之後 0.5 s 才給氣味，所以第一下光在氣味開始前 2.0 s）無效。這足以說明「順序有關」，**不足以支持摘要的「strictly depends」與討論的「sub-second precision」**：沒有測任何中間間隔，也沒有測氣味與光同時開始。反向組的尖峰數略升（OCT 約 95 → 100，※ 從圖判讀），但不顯著，論文沒有主張反向會引發增強。
- **要看 E 格配對後 OCT 曲線的起頭。** 配對後仍有一個約 50 spikes/s 的起始暫態，之後才幾乎歸零（※ 從圖判讀）。抑制作用在持續段，不在開頭。這一點在圖 3、6、7 重複出現，論文全文沒有討論（搜過 transient、peak、initial、early）。它重要的原因見 3.3 與「五、問題與限制」第 8 條。

#### 3.2 KC 的反應沒有改變（圖 2）

![Figure 2：氣味–多巴胺配對不改變 KC 的氣味反應](../../assets/hige2015-fig2.jpg)

<small>圖片出處：Hige T, Aso Y, Modi MN, Rubin GM, Turner GC. *Neuron* 88(5):985–998 (2015)，Figure 2。© 2015 Elsevier Inc. 教學引用；全文見 [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4674068/)。</small>

> **原圖說（Figure 2）：** Odor-Dopamine Pairing Does Not Change KC Odor Responses. (A–D) Trial-averaged time courses (4 trials) of odor responses (ΔF/F, grayscale) in KC somata before (A and C) and after (B and D) 1 s odor-light pairing. Data from a single representative fly. Each row corresponds to a single KC. Colored bars, 1 s odor presentation. (E) Median response amplitude for each significantly responding cell before and after pairing. Red and green points indicate CS+ (OCT; n = 53 cells from 5 flies) and CS− (MCH; n = 49), respectively. Gray points are from control experiments where no light pulses were delivered (OCT and MCH; n = 32 from 2 flies). Error bar, median absolute deviation. Solid lines, linear regressions. Dashed line, unity. All three datasets showed a small but significant decrease after pairing (p < 0.05, paired t test). (F) Histograms of the change in response magnitude (ΔF/F) after pairing (pre subtracted from post). Only cells that significantly responded to the odor in either pre- or post-pairing recordings were included. There was no difference between any combination of the distributions of CS+ responses (red), CS− (green), and control (gray; Kolmogorov Smirnov test, p > 0.1). (G) Single-trial responses projected onto the space of the first two principal components. Data from a single representative fly. Responses from pre- (lighter colors) and post-pairing trials (darker colors) are intermingled, while CS+ (red) and CS− (green) are well separated. (H) Comparing population response patterns pre- and post-training. Euclidean distances between each post-pairing trial and the centroid of pre-pairing trials calculated in the full n-dimensional neuronal representation space are plotted, where n corresponds to the number of neurons imaged in each fly. Distances were normalized to the distance from the origin to the centroid of the pre-pairing trials. There was no significant difference between CS+ (red) and CS− (green; p = 0.58, unpaired t test). See also Experimental Procedures.

**圖說中譯：** 氣味–多巴胺配對不改變 KC 的氣味反應。(A–D) KC 細胞體氣味反應（ΔF/F，灰階）的試驗平均時間過程（4 次），配對前（A、C）與 1 s 氣味–光配對後（B、D）；單一代表果蠅；每列一顆 KC；色條為 1 s 氣味。(E) 每顆顯著反應細胞配對前後的反應振幅中位數。紅點為 CS+（OCT；5 隻果蠅共 53 顆細胞），綠點為 CS−（MCH；n = 49）；灰點為不給光的對照（OCT 與 MCH；2 隻共 32 顆）。誤差棒為中位數絕對差；實線為線性回歸；虛線為對角線。三組在配對後都有小而顯著的下降（p < 0.05，成對 t 檢定）。(F) 配對後反應幅度變化（後減前）的直方圖，只納入配對前或後顯著反應的細胞；CS+（紅）、CS−（綠）、對照（灰）任兩者的分布都無差異（Kolmogorov–Smirnov 檢定，p > 0.1）。(G) 單次試驗反應投影到前兩個主成分的空間；單一代表果蠅；配對前（淺色）與配對後（深色）混在一起，而 CS+（紅）與 CS−（綠）分得很開。(H) 比較訓練前後的族群反應樣式：在完整的 n 維神經元表徵空間（n 為該果蠅成像的細胞數）中，計算每次配對後試驗到配對前試驗重心的歐氏距離，並以原點到重心的距離標準化；CS+ 與 CS− 無顯著差異（p = 0.58，非成對 t 檢定）。

> 註：原圖說 (A–D) 寫「before (A and C) and after (B and D)」，但圖面上 A／C 是 Pre／Post 的 OCT，B／D 是 Pre／Post 的 MCH，配對前應為 A 與 B、配對後為 C 與 D。⚠️ 論文自身不一致（圖說字母與圖面配置對不上；不影響結論）。

**解讀：**

- **本圖在全文論證中的角色**：MBON 的反應變小，可能是 KC 與 MBON 之間的突觸變弱，也可能只是 KC 本身對氣味的反應變弱了。本圖用兩類方式檢查後者：E、F 看每顆 KC 的反應大小（F 的三組分布沒有差異，表示配對沒有在一般性的小幅下降之外，額外改變 KC 的反應）；G、H 看整群 KC 的反應樣式（H 問的是 CS+ 的樣式在配對後是否比 CS− 移動得更多，結果沒有）。兩類檢查都沒有找到 CS+ 專屬的改變，於是作者把改變定位在 KC 與 MBON 之間，再由圖 3 直接量突觸電流。
- **反應比例可以算出來：約 12–13%。** E 格的 53 顆（OCT）與 49 顆（MCH）來自 5 隻果蠅，平均每隻約 10–11 顆；方法說每隻圈出 82 ± 9 顆（n = 7 隻，含 2 隻對照）。53 ÷ (5 × 82) ≈ 13%、49 ÷ 410 ≈ 12%。這與「稀疏」的說法一致。3.1 重疊估算所用的 30%／33%，很可能也是從這批細胞算出來的（依據見下一條的推論）。※ 推論：用 82 當作 5 隻配對果蠅的平均是近似值。
- **第 990 頁的 30%／33% 重疊與本圖的細胞數互相吻合。** 0.30 × 53 ≈ 15.9、0.33 × 49 ≈ 16.2，即約 16 顆細胞同時對兩種氣味反應。論文沒有說 30%／33% 是從哪批資料算的（圖 7I 的重疊值則明說來自 Campbell et al. 2013）；數字對得上，暗示它來自本圖的資料。※ 推論。
- **對照組（不給光）同樣下降，這是本圖最重要的設計。** 三條回歸線都在對角線下方，且三者幾乎重疊；作者歸因於光漂白與光損傷（成像時雷射反覆照射，螢光蛋白逐漸變暗，與是否給紅光無關）。沒有灰色組，紅色組的下降就會被誤讀為「KC 也有可塑性」。
- **踩煞車：本圖量的是細胞體，不是 γ1 區的軸突末梢。** 細胞體的鈣訊號反映整顆細胞的放電，不反映某一個區室裡突觸前末梢的釋放。所以本圖排除的是「KC 整體的反應或興奮性改變」，**沒有排除「突觸前末梢在 γ1 局部改變了釋放」**。作者在討論中提到 Boto et al. 2014 在 γ1 末梢看不到鈣變化，並列出三種可能的解釋，沒有裁定（見「五、問題與限制」第 3 條）。
- **樣本小**：配對組 5 隻、對照組 2 隻，CS+ 只用 OCT。KC 興奮性的直接測試（γ KC 全細胞記錄，圖 S7）的 n 與數值 ？待查（補充資料未取得）。

#### 3.3 突觸電荷少了九成（圖 3）

本節的「九成」指的是電荷轉移（0–1.4 s 內電流的時間積分）下降約九成，不是電流峰值下降九成；兩者的差別是本節解讀的重點。

![Figure 3：氣味與 DAN 活化配對引發突觸 LTD](../../assets/hige2015-fig3.jpg)

<small>圖片出處：Hige T, Aso Y, Modi MN, Rubin GM, Turner GC. *Neuron* 88(5):985–998 (2015)，Figure 3。© 2015 Elsevier Inc. 教學引用；全文見 [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4674068/)。</small>

> **原圖說（Figure 3）：** Pairing of Odor and DAN Activation Induces Synaptic LTD. (A) Expression of CsChrimson and GFP was driven by MB320C and R12G04-LexA, respectively. Whole-cell voltage-clamp recordings were made from MBON-γ1pedc. Action potentials were completely suppressed by QX-314 in the pipette solution. (B) Representative voltage-clamp data from a single cell, showing odor-evoked EPSCs before (Pre) and after (Post) pairing. Gray bar, 1 s odor presentation. Overlaid traces (bottom) show mean EPSCs pre- and post-pairing in this cell (n = 5–7 trials). Scale bar, 200 pA. (C) Mean EPSCs (±SEM, shaded area; n = 5 cells). (D) Mean charge transfer of EPSC (±SEM). Gray lines indicate data from individual flies. Excitatory synaptic input decreased for CS+ (p < 0.005, Tukey's post hoc test following repeated-measures two-way ANOVA), but not for CS− (p > 0.1).

**圖說中譯：** 氣味與 DAN 活化配對引發突觸長期抑制（LTD）。(A) 以 MB320C 驅動 CsChrimson、R12G04-LexA 驅動 GFP；對 MBON-γ1pedc 做全細胞電壓箝制記錄；電極內液中的 QX-314 完全抑制了動作電位。(B) 單一細胞的電壓箝制代表資料，配對前後的氣味誘發 EPSC；灰條為 1 s 氣味；下方疊圖為該細胞配對前後的平均 EPSC（5–7 次試驗）；比例尺 200 pA。(C) 平均 EPSC（±SEM，陰影；n = 5 顆細胞）。(D) EPSC 的平均電荷轉移（±SEM）；灰線為個別果蠅。CS+ 的興奮性突觸輸入下降（p < 0.005，重複量測雙因子 ANOVA 後的 Tukey 事後檢定），CS− 則否（p > 0.1）。

**解讀：**

- **正文與圖的描述方向不同。** 正文說配對後 EPSC「dramatically reduced early in the response」，並且後段幾乎沒有持續電流。但 B、C 兩格的平均軌跡顯示，**起始的峰值大致保留（配對後峰值約為配對前的八、九成，※ 從圖判讀），被拿掉的是峰值之後的持續成分**。電荷轉移（時間積分）下降約九成，主要就是持續段消失所致。這與圖 1E 尖峰的起始暫態仍在是同一件事。⚠️ 論文自身不一致（正文措辭與圖；也可能 "early" 指峰值後衰減得早，原文有歧義）。
- **起始峰為什麼不受影響，是本篇留下的開口。** ※ 推論，三種可能，論文都沒有討論：(1) 起始峰來自不經過 γ1 區 KC–MBON 突觸的其他輸入；(2) 依作者的模型，只有「多巴胺到達時正在活動」的 KC 突觸會被削弱；若氣味一開始只短暫放電的 KC，在第一下光（0.2 s）到達前已經停止活動，它們的突觸就不會被削弱，而它們貢獻的正是起始峰；(3) 抑制只作用於持續釋放的機制。
- **CS+ 約 250 → 25 pC，CS− 約 275 → 220 pC**（※ 從圖判讀）。CS− 下降約 20%，在 n = 5 下不顯著。這與圖 1 中 CS− 尖峰數下降 25%（n = 7，顯著）幅度相近，**差別可能只是統計檢定力不同**，不宜解讀為「突觸電流層級完全專一、尖峰層級不專一」。※ 推論。
- **對過度解讀踩煞車**：作者自己在正文與討論都保留了「MBON 上游的其他元件（例如 DPM 神經元）也可能貢獻」的可能性。九成的降幅只說明「主要輸入」被改變了，而 KC 是預期的主要輸入。

#### 3.4 不需要突觸後放電（圖 4）

![Figure 4：LTD 的誘發不需要突觸後尖峰](../../assets/hige2015-fig4.jpg)

<small>圖片出處：Hige T, Aso Y, Modi MN, Rubin GM, Turner GC. *Neuron* 88(5):985–998 (2015)，Figure 4。© 2015 Elsevier Inc. 教學引用；全文見 [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4674068/)。</small>

> **原圖說（Figure 4）：** Postsynaptic Spikes Are Dispensable for LTD Induction. (A) Expression of CsChrimson and GFP was driven by MB320C and R12G04-LexA, respectively. Whole-cell recordings were made from MBON-γ1pedc. (B) After recording baseline odor responses in current-clamp mode, recording mode was switched to voltage clamp to record EPSCs. Odor-light pairing (1 s odor with 1 ms light pulses × 4) was performed under voltage-clamp mode, which suppressed 83% ± 4.5% of odor-evoked spikes (mean ± SEM, n = 6). After pairing, spikes and EPSCs were recorded by flipping the mode between current-clamp and voltage-clamp. (C) Representative current-clamp data from a single cell, showing odor responses before (Pre) and after (Post) pairing. Gray bar, 1 s odor presentation. Scale bar, 20 mV. Raster plots (bottom) show spikes. (D) Mean PSTH (±SEM, shaded area; n = 6). (E) Mean odor-evoked spike count (±SEM). Gray lines indicate data from individual flies. Spike counts decreased in both CS+ (p < 0.001, Tukey's post hoc test) and CS− (p < 0.01), but the effect of pairing was significantly different between the two odors (p < 0.005, repeated-measures two-way ANOVA). (F) Representative voltage-clamp data from the same cell shown in (C). Currents evoked by unclamped spikes were truncated for display. Mean EPSCs (3 trials) after filtering out unclamped spikes are also shown (bottom). Scale bar, 200 pA. (G) Mean filtered EPSCs (±SEM, shaded area; n = 6). (H) Mean charge transfer (±SEM). Gray lines indicate data from individual flies. Charge transfer decreased in CS+ (p < 0.001, Tukey's post hoc test) and CS− (p < 0.001), but the effect of pairing was significantly different between the two odors (p < 0.005, repeated-measures two-way ANOVA).

**圖說中譯：** LTD 的誘發不需要突觸後尖峰。(A) 以 MB320C 驅動 CsChrimson、R12G04-LexA 驅動 GFP；對 MBON-γ1pedc 做全細胞記錄。(B) 先以電流箝制記錄基線氣味反應，再切換到電壓箝制記錄 EPSC。氣味–光配對（1 s 氣味配 1 ms 光脈衝 × 4）在電壓箝制下進行，抑制了 83% ± 4.5% 的氣味誘發尖峰（mean ± SEM，n = 6）。配對後在電流箝制與電壓箝制間切換，分別記錄尖峰與 EPSC。(C) 單一細胞的電流箝制代表資料；灰條為 1 s 氣味；比例尺 20 mV；下方光柵圖為尖峰。(D) 平均 PSTH（±SEM，陰影；n = 6）。(E) 平均氣味誘發尖峰數（±SEM）；灰線為個別果蠅。CS+（p < 0.001，Tukey）與 CS−（p < 0.01）都下降，但配對效果在兩種氣味間顯著不同（p < 0.005，重複量測雙因子 ANOVA）。(F) 與 (C) 同一細胞的電壓箝制資料；未箝住的尖峰所引起的電流在顯示時截斷；下方為濾除未箝住尖峰後的平均 EPSC（3 次）；比例尺 200 pA。(G) 濾波後的平均 EPSC（±SEM，陰影；n = 6）。(H) 平均電荷轉移（±SEM）；灰線為個別果蠅。CS+（p < 0.001，Tukey）與 CS−（p < 0.001）都下降，但配對效果在兩種氣味間顯著不同（p < 0.005，重複量測雙因子 ANOVA）。

**解讀：**

- **為什麼要做這個實驗。** 蝗蟲的 KC–MBON 可塑性是 Hebbian STDP，需要 MBON 放電。果蠅行為研究則顯示，訓練時阻斷 KC 的輸出（KC 照常活動，只是不把訊號送給 MBON，所以 MBON 在訓練中幾乎不會被 KC 驅動放電）仍能學習（Dubnau et al. 2001 等），暗示誘發不需要 MBON 放電。圖 3 已用 QX-314 消除 MBON 尖峰並看到突觸電荷的 LTD，這支持「誘發不需要尖峰」。但作者指出圖 3 留下一個缺口：圖 1 看到的是**尖峰數**下降，而 QX-314 下量不到尖峰，所以無法排除「MBON 尖峰有部分參與了圖 1 那種尖峰數的下降」（正文第 989 頁）。本圖改用不加 QX-314 的內液，配對時以電壓箝制把尖峰壓低，事後在同一顆細胞上切換模式，既量尖峰也量 EPSC。
- **CS− 在本圖的突觸電流層級也顯著下降，與圖 3 不同。** 圖 3D 的 CS− 不顯著（p > 0.1），本圖 H 的 CS− p < 0.001；從圖判讀，CS− 電荷由約 240 降到 155 pC（約 −35%），尖峰由約 108 降到 68（約 −37%），都比圖 1 的 −25% 大。正文說本圖的 EPSC LTD「與圖 3 相似」，只就 CS+ 而言成立。就專一性而言：CS+ 的降幅仍顯著大於 CS−（兩因子交互作用 p < 0.005），所以「CS+ 受影響較大」成立，「只有 CS+ 受影響」不成立。⚠️ 論文自身不一致（CS− 在兩個 EPSC 實驗中顯著性相反，正文未說明）。
- **CS+ 的電荷轉移在本圖約 255 → 60 pC（約 −76%）**，比圖 3 的 −90% 小（※ 從圖判讀）。兩圖的量法不同：本圖不用 QX-314，記錄中仍有未被箝住的尖峰造成的電流突波，作者以 100 Hz 低通濾波去除後才算電荷；圖 3 則用 QX-314 與銫內液。※ 推論：降幅差異可能來自量法，也可能只是不同批細胞的差異，論文沒有比較兩者。
- **踩煞車**：配對期間仍有 17% 的尖峰沒被抑制（100% − 83%）。所以本圖嚴格說明的是「把尖峰壓到兩成以下仍誘發同樣的 LTD」，完全不需尖峰的證據來自圖 3（QX-314）。兩者合起來才構成作者的結論。

#### 3.5 區室各自獨立（圖 5）

![Figure 5：DAN 誘發的可塑性有區室專一性](../../assets/hige2015-fig5.jpg)

<small>圖片出處：Hige T, Aso Y, Modi MN, Rubin GM, Turner GC. *Neuron* 88(5):985–998 (2015)，Figure 5。© 2015 Elsevier Inc. 教學引用；全文見 [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4674068/)。</small>

> **原圖說（Figure 5）：** DAN-Induced Plasticity Is Compartment Specific. (A) Expression of CsChrimson and GFP was driven by MB099C and R12G04-LexA, respectively. Recordings were made from MBON-γ1pedc. (B) Representative single-cell data, showing odor responses before (Pre) and after (Post) pairing. Gray bar, 1 s odor presentation. Scale bar, 20 mV. Raster plots (bottom) show spikes. (C) Mean PSTH (±SEM, shaded area; n = 8). (D) Mean odor-evoked spike count (±SEM). Gray lines indicate data from individual flies. Pairing had no significant effect (p > 0.05, repeated-measures two-way ANOVA). (E) Expression of CsChrimson was driven by TH-GAL4, which labels a broad subset of PPL1 DANs, including PPL1-γ1pedc, and a few PAM DANs as well as many other DANs outside the MB (not shown). Recordings were made from MBON-γ1pedc. (F) Representative single-cell data. (G) Mean PSTH (n = 5). (H) Mean odor-evoked spike count. Spike counts decreased in both CS+ (p < 0.01, Tukey's post hoc test) and CS− (p < 0.01), but the effect of pairing was significantly different between the two odors (p < 0.05, repeated-measures two-way ANOVA). (I) Expression of CsChrimson and GFP was driven by MB320C and R25D01-LexA, respectively. Recordings were made from MBON-γ2α′1. (J) Representative single-cell data. (K) Mean PSTH (n = 6). (L) Mean odor-evoked spike count. Pairing showed no effect (p > 0.1, repeated-measures two-way ANOVA).

**圖說中譯：** DAN 誘發的可塑性有區室專一性。(A) 以 MB099C 驅動 CsChrimson、R12G04-LexA 驅動 GFP；記錄 MBON-γ1pedc。(B) 單一細胞代表資料；灰條為 1 s 氣味；比例尺 20 mV；下方光柵圖為尖峰。(C) 平均 PSTH（±SEM，陰影；n = 8）。(D) 平均氣味誘發尖峰數（±SEM）；灰線為個別果蠅；配對無顯著效果（p > 0.05，重複量測雙因子 ANOVA）。(E) 以 TH-GAL4 驅動 CsChrimson；TH-GAL4 標記多數 PPL1 DAN（含 PPL1-γ1pedc）、少數 PAM DAN，以及 MB 以外的許多 DAN（未示）；記錄 MBON-γ1pedc。(F) 單一細胞代表資料。(G) 平均 PSTH（n = 5）。(H) 平均氣味誘發尖峰數；CS+（p < 0.01，Tukey）與 CS−（p < 0.01）都下降，但配對效果在兩種氣味間顯著不同（p < 0.05，重複量測雙因子 ANOVA）。(I) 以 MB320C 驅動 CsChrimson、R25D01-LexA 驅動 GFP；記錄 MBON-γ2α′1。(J) 單一細胞代表資料。(K) 平均 PSTH（n = 6）。(L) 平均氣味誘發尖峰數；配對無效果（p > 0.1，重複量測雙因子 ANOVA）。

**解讀：**

- **這張圖有兩個方向的實驗，邏輯不同。** A–D 是「活化鄰區 DAN，本區 MBON 不變」（多巴胺不外溢到鄰區）。這裡用的 MB099C，依本篇所述標記四型 PPL1 DAN（PPL1-γ2α′1、α′2α2、α′3、α3），從不標記 PPL1-γ1pedc。⚠️ 矛盾｜[[s-aso-2016-dan-cell-type-rules]] 說同一品系只標記 PPL1-γ2α′1 與 PPL1-α′2α2 兩型｜未裁決，見 [[syn-contradictions]] 1.4（2026-10-25 第二批加註）；不論哪一種說法，都不含 PPL1-γ1pedc。四型中與 γ1 相鄰的是投射到 γ2 的那一型。E–H 是正對照（TH-GAL4 以 TH 基因〔酪胺酸羥化酶，tyrosine hydroxylase，合成多巴胺的酵素〕的調控序列驅動表現，依圖說標記PPL1 群中的**一大部分**（原文 a broad subset of PPL1 DANs，不是「多數」）、少數 PAM DAN 及 MB 以外的許多 DAN；只要包含 PPL1-γ1pedc 就有效），I–L 是「本區誘發 LTD，鄰區 MBON 不變」（同一條 KC 軸突上的訊號不沿軸突擴散到下一個區室）。兩者檢驗的是兩種不同的「外溢」。A–D 問的是細胞**外**：DAN 在 γ2 區釋放的多巴胺，會不會擴散到隔壁的 γ1 區。I–L 問的是細胞**內**：γ1 區的多巴胺活化 KC 軸突上的受器後，軸突內的第二傳訊者會不會沿著同一條軸突擴散到 γ2 區，連帶改變 KC 通往 MBON-γ2α′1 的突觸。後者較難預測，因為兩個區室共用同一批 KC 軸突，所以這個陰性結果更有份量。
- **I–L 的陰性結果有一個論文沒處理的替代解釋。** 本篇第 3.6 節自己證明了不同區室的誘發門檻不同（α2 要 1 分鐘）。所以「γ1 誘發 LTD 時 γ2α′1 不變」有兩種讀法：多巴胺的作用真的沒有擴散；或者有微量擴散，但不足以跨過 γ2 區的誘發門檻。γ2 區的門檻不一定與 γ1 相同（α2 區的門檻就比 γ1 高），本篇沒有測 γ2 區自己的門檻，無法區分。※ 推論。
- **檢定力**：L 格 n = 6，個別果蠅的線方向分散，CS+（OCT）尖峰數平均約 105 → 91（約 −13%，※ 從圖判讀）。這個 n 能排除「像 γ1 那樣八成的下降」，排除不了一、二成的小變化。
- **基線差異**：A–D（MB099C）的 MBON-γ1pedc 基線約 75 spikes（OCT），明顯低於圖 1 的 118（※ 從圖判讀）。基因型不同，論文沒有評論。這不推翻 A–D 的陰性結論，但表示不同品系的 MBON 起點不同，跨圖比較絕對尖峰數時要小心。
- **TH-GAL4 與另一篇研究的對照**：E–H 這組正對照用的 TH-GAL4，恰好也是另一篇研究用的品系。作者在討論中指出，Boto et al. 2014 用同一個 TH-GAL4 在 γ1 的 KC 軸突上看不到鈣反應變化，而本篇看到強烈 LTD。推理是：若 LTD 來自 KC 末梢少送了訊號，預期末梢的鈣反應也會變小；Boto 沒看到變小，所以兩者對不上，作者也承認這一點（三種可能的解釋見「五、問題與限制」第 3 條）。這是本篇唯一一處把自己的突觸結果與突觸前的成像結果正面並列。

#### 3.6 區室之間規則不同（圖 6）

![Figure 6：不同區室的可塑性規則不同](../../assets/hige2015-fig6.jpg)

<small>圖片出處：Hige T, Aso Y, Modi MN, Rubin GM, Turner GC. *Neuron* 88(5):985–998 (2015)，Figure 6。© 2015 Elsevier Inc. 教學引用；全文見 [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4674068/)。</small>

> **原圖說（Figure 6）：** Plasticity Rule Is Different across Compartments. (A) Expression of CsChrimson and GFP was driven by MB099C and R34B02-LexA, respectively. Recordings were made from MBON-α2sc. (B) Representative single-cell data, showing odor responses before (Pre) and after (Post) 1 s pairing. Gray bar, 1 s odor presentation. Scale bar, 20 mV. Raster plots (bottom) show spikes. (C) Mean PSTH (±SEM, shaded area; n = 7). (D) Mean odor-evoked spike count (±SEM). Gray lines indicate data from individual flies. Pairing showed no effect (p > 0.1, Tukey's post hoc test following repeated-measures two-way ANOVA). (E) 1 min pairing protocol. (F) Representative single-cell data. (G) Mean PSTH (n = 6). (H) Mean odor-evoked spike count. Spike counts decreased in CS+ (p < 10⁻⁵, Tukey's post hoc test), but not in CS− (p > 0.1), and the effect of pairing was significantly different between the two odors (p < 0.001, repeated-measures two-way ANOVA).

**圖說中譯：** 不同區室的可塑性規則不同。(A) 以 MB099C 驅動 CsChrimson、R34B02-LexA 驅動 GFP；記錄 MBON-α2sc。(B) 1 s 配對前後的單一細胞代表資料；灰條為 1 s 氣味；比例尺 20 mV；下方光柵圖為尖峰。(C) 平均 PSTH（±SEM，陰影；n = 7）。(D) 平均氣味誘發尖峰數（±SEM）；灰線為個別果蠅；配對無效果（p > 0.1，重複量測雙因子 ANOVA 後的 Tukey 事後檢定）。(E) 1 分鐘配對協定。(F) 單一細胞代表資料。(G) 平均 PSTH（n = 6）。(H) 平均氣味誘發尖峰數；CS+ 下降（p < 10⁻⁵，Tukey），CS− 則否（p > 0.1），配對效果在兩種氣味間顯著不同（p < 0.001，重複量測雙因子 ANOVA）。

**解讀：**

- **兩個協定同時改了兩件事。** 1 s 協定：1 s 氣味 ＋ 4 個光脈衝；1 min 協定：60 s 氣味 ＋ 120 個光脈衝。氣味時間長了 60 倍、光脈衝多了 30 倍。所以「α2 需要更長的配對」可能是需要更多多巴胺、更長的 KC 活動，或兩者都要，本篇分不開。E 格也顯示，1 min 協定中 CS−（MCH）在配對後同樣單獨給了 60 s（不配光），讓兩種氣味的曝露時間相同；所以 CS− 的曝露也變長了。
- **門檻差距只能給下界。** γ1pedc 用單一 1 ms 脈衝就能誘發強 LTD（圖 7 與圖 S6F），α2 用 4 個脈衝不行、120 個可以。所以 α2 的門檻落在「多於 4 個、至多 120 個脈衝」之間，而 γ1 只要 1 個就夠（它真正的門檻沒有測到更低）。兩者相差**超過 4 倍，上限未知**。標題的「Plasticity Rule Is Different」實際量到的是誘發門檻（需要多少配對才會發生）的差異，不是規則形式（例如時序要求或改變方向）的差異。
- **驅動品系不同是一個混淆因子。** α2 用的是 MB099C（同時活化四型 PPL1 DAN），γ1 用的是 MB320C（只有一顆）。兩者的 CsChrimson 表現量、每顆 DAN 每個脈衝釋放的多巴胺量都可能不同。作者以圖 S2B 確認光脈衝能讓 PPL1-α′2α2 放電，但放電的可靠度能否與 γ1 相比 ？待查（補充資料未取得）。若 α2 的 DAN 每個光脈衝放電較少，「α2 門檻較高」就可能只是「α2 的 DAN 被光活化得較弱」。作者自己也承認「PPL1-α′2α2 可能在不同刺激條件下誘發可塑性」，並引行為資料（圖 S1F：以 MB099C 的光活化取代電擊來訓練果蠅，效果遠低於 MB320C）支持門檻差異是真的。
- **1 min 協定在 α2 的抑制非常乾淨**：CS+ 約 74 → 5，CS− 約 66 → 58（※ 從圖判讀），比 γ1 的 1 s 協定更專一。

#### 3.7 KC 重疊決定干擾與類化（圖 7）

本節檢驗的邏輯：配對只削弱「CS+ 活化的那批 KC」通往 MBON 的突觸。另一種氣味若與 CS+ 共用一部分 KC（重疊），它的訊號也有一部分走被削弱的突觸，於是被連帶抑制（突觸干擾）。重疊越多，波及越大；行為上的對應就是類化。

![Figure 7：突觸干擾與嗅覺類化](../../assets/hige2015-fig7.jpg)

<small>圖片出處：Hige T, Aso Y, Modi MN, Rubin GM, Turner GC. *Neuron* 88(5):985–998 (2015)，Figure 7。© 2015 Elsevier Inc. 教學引用；全文見 [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4674068/)。</small>

> **原圖說（Figure 7）：** Synaptic Interference and Olfactory Generalization. (A) Expression of CsChrimson and GFP was driven by MB320C and R12G04-LexA, respectively. Recordings were made from MBON-γ1pedc. (B) Chemical structures of the test odors. PA, pentyl acetate; BA, butyl acetate; HP, 2-heptanone; EL, ethyl lactate. (C) Representative single-cell data, showing odor responses before (Pre) and after (Post) pairing with PA. Gray bar, 1 s odor presentation. Gray line, −60 mV. Scale bar, 20 mV. Raster plots (bottom) show spikes. (D) Mean PSTH (±SEM, shaded area; n = 7). (E) Mean odor-evoked spike count (±SEM). Gray lines indicate data from individual flies. Depression was significant for PA, BA, and HP (p < 0.005, Tukey's post hoc test following repeated-measures two-way ANOVA), but not for EL (p > 0.1). Depression of PA was slightly stronger than BA and HP (p < 0.05, paired t test). (F) Representative single-cell data for pairing with EL. (G) Mean PSTH (n = 5). (H) Mean odor-evoked spike count. Depression was significant for EL (p < 0.01, Tukey's post hoc test following repeated-measures two-way ANOVA) and HP (p < 0.05), but not for the others (p > 0.05). Depression of EL was stronger than HP (p < 0.05, paired t test). (I) Magnitude of depression correlates with extent of overlap in KC response patterns (p < 0.005, Pearson's r = 0.90). Each point shows the response depression for a different odor with the indicated degree of overlap with the CS+ KC response pattern (overlap calculated from data in Campbell et al., 2013). Error bars, SEM. Gray line, linear regression. (J) Behavioral test for odor generalization. Flies were presented with PA and light in a paired or unpaired manner (see Figure S1) and subsequently tested for aversive learning with one of the three different combinations of odors. (K) Performance index (PI). Positive PI indicates relative avoidance of PA, BA, or HP when flies are given the choice between those odors and EL. Flies generalized their avoidance of PA to the other odors (n = 10 for each; p < 0.01, Tukey's post hoc test following two-way ANOVA).

**圖說中譯：** 突觸干擾與嗅覺類化。(A) 以 MB320C 驅動 CsChrimson、R12G04-LexA 驅動 GFP；記錄 MBON-γ1pedc。(B) 測試氣味的化學結構：PA 乙酸戊酯、BA 乙酸丁酯、HP 2-庚酮、EL 乳酸乙酯。(C) 以 PA 配對前後的單一細胞代表資料；灰條為 1 s 氣味；灰線為 −60 mV；比例尺 20 mV；下方光柵圖為尖峰。(D) 平均 PSTH（±SEM，陰影；n = 7）。(E) 平均氣味誘發尖峰數（±SEM）；灰線為個別果蠅。PA、BA、HP 的抑制顯著（p < 0.005，重複量測雙因子 ANOVA 後的 Tukey），EL 則否（p > 0.1）；PA 的抑制略強於 BA 與 HP（p < 0.05，成對 t 檢定）。(F) 以 EL 配對的單一細胞代表資料。(G) 平均 PSTH（n = 5）。(H) 平均氣味誘發尖峰數；EL（p < 0.01）與 HP（p < 0.05）的抑制顯著，其餘不顯著（p > 0.05）；EL 的抑制強於 HP（p < 0.05，成對 t 檢定）。(I) 抑制幅度與 KC 反應樣式的重疊程度相關（p < 0.005，Pearson r = 0.90）。每點為一種氣味的反應抑制，橫軸為它與 CS+ 的 KC 反應樣式的重疊程度（重疊由 Campbell et al. 2013 的資料計算）；誤差棒為 SEM；灰線為線性回歸。(J) 嗅覺類化的行為測試：果蠅接受 PA 與光的配對或不配對呈現（見圖 S1），之後以三種氣味組合之一測試嫌惡學習。(K) 學習表現指數（performance index, PI）。PI 為正表示在 PA、BA 或 HP 與 EL 之間選擇時，相對迴避前者；果蠅把對 PA 的迴避類化到其他氣味（每組 n = 10；p < 0.01，雙因子 ANOVA 後的 Tukey 事後檢定）。

**解讀：**

- **I 格的軸**：橫軸是某種氣味與 CS+ 的 KC 反應重疊程度（0 到 1；1 表示完全相同），縱軸是該氣味配對後被抑制的比例（0 到 1；0.8 表示尖峰數少了八成）。
- **r = 0.90 有兩個點是定義上必然落在右上角的。** I 格共 8 個點：PA 配對時的 BA、HP、EL，EL 配對時的 PA、BA、HP，加上兩個 CS+ 自己（PA 配 PA、EL 配 EL）。CS+ 與自己的重疊必然是 1，而 CS+ 正是被配對、抑制最強的氣味，所以這兩點必然落在右上角；它們在 x = 1 處疊在一起（※ 從圖判讀）。依圖讀出的 8 點座標重算，r ≈ 0.90（p ≈ 0.003），與論文一致；**去掉兩個自身點後，6 點的 r ≈ 0.85（p ≈ 0.03）**。相關仍在，但證據強度降了一個等級，而且 6 點分成兩群（重疊 0.1–0.3 的四點、0.44 與 0.63 的兩點），中間沒有資料。這比較像「高重疊組 vs 低重疊組」的兩組比較，而不是一條連續的劑量反應曲線。※ 推論；座標為從圖判讀，可能有 ±0.02 的誤差。
- **H 格與論文正文的措辭有落差。** 論文正文（第 992 頁）說 EL 配對後「其他三種氣味變化很小」（changed very little），但 HP 顯著下降（p < 0.05），PA 與 BA 從圖讀約下降 23–28%（PA 約 100 → 72、BA 約 98 → 75；※ 從圖判讀），**與圖 1 中 MCH 被稱為「slightly, but significantly」的 27% 同一量級**。差別在 n（5 vs 7）。同樣的效果量，一處叫「顯著」、一處叫「很小」。
- **單脈衝協定**：本圖改用較溫和的 1 ms × 1 脈衝（於 CS+ 開始後 0.8 s）。作者以 OCT／MCH 測過：多巴胺刺激變少後，CS+ 仍有強烈 LTD，而 CS− 被連帶抑制的幅度從 27% ± 7.1% 降為 20% ± 6.3%（圖 S6G–I）。選這個協定，是為了讓「被波及」的部分更能反映 KC 重疊，而不是刺激過強。所以本圖與圖 1 的協定不同，不能直接並排比較抑制幅度。
- **行為與生理的類化比例不同。** 兩者單位不同，所以各自換算成「相對於 PA 的比例」再比。生理：I 格縱軸（抑制比例）上，BA、HP 的點約 0.66 與 0.69，PA 自身約 0.80，所以 BA、HP 被抑制的程度約為 PA 的 83–86%。（若改用 E 格長條的平均值換算，BA 約 0.73、HP 約 0.67、PA 約 0.84，略有出入；I 格應是逐隻果蠅比例的平均，長條換算的是平均值的比例，兩者本來就不必相等。※ 推論。兩種算法下 BA、HP 都約為 PA 的八成上下。）行為：BA 的 PI 約 42、HP 約 38，PA 約 67（※ 從圖判讀），即 BA、HP 的迴避約為 PA 的 55–65%。**行為上的類化比 γ1 突觸層級的波及弱。** ※ 推論：行為由多個區室的 MBON 共同決定，本篇只量了 γ1pedc 一個區室；若其他區室的 MBON 對相似氣味的區分較好，總和起來的類化就會比 γ1 單獨看到的弱。
- **行為設計只測了一個方向。** 測試時永遠是「PA／BA／HP 對 EL」，沒有測「PA 對 BA」這種相似氣味之間的辨別，也沒有做以 EL 為 CS+ 的反向訓練。行為的光刺激（500 ms × 12，從 J 格讀出）與生理（1 ms × 1）完全不同。
- **最重要的一點**：圖 7 的生理與行為是不同的果蠅、不同的協定。「類化是由突觸干擾所介導」（論文本節最後一句：「was indeed mediated by synaptic interference」）是兩組相關的對應，**沒有做「阻斷 γ1 的 LTD 就消除類化」這種因果實驗**。

#### 3.8 各實驗總表（重製）

| 實驗（圖） | DAN 驅動品系 | 記錄的 MBON | 協定 | n | CS+（配對氣味）前 → 後 | 未配對氣味 前 → 後 | 結果 |
|---|---|---|---|---:|---|---|---|
| 正向配對（1F） | MB320C | γ1pedc | 1 s，1 ms × 4 | 7 | 118 ± 8.3 → 24 ± 7.4 spikes | 110 ± 11 → 83 ± 14 | CS+ −80% ± 5.7%；CS− −27% ± 7.1%（皆顯著） |
| 反向配對（1J） | MB320C | γ1pedc | 光先、末次光後 0.5 s 給氣味 | 7 | 約 95 → 100* | 約 82 → 80* | 無效果 |
| EPSC，QX-314（3D） | MB320C | γ1pedc | 1 s，1 ms × 4 | 5 | 約 250 → 25 pC*（−90% ± 3.7%） | 約 275 → 220 pC* | CS− 不顯著 |
| 電壓箝制下配對（4E、4H） | MB320C | γ1pedc | 同上，尖峰被抑 83% ± 4.5% | 6 | 約 115 → 17 spikes*；約 255 → 60 pC* | 約 108 → 68*；約 240 → 155 pC* | CS− 兩項皆顯著 |
| 鄰區 DAN（5D） | MB099C | γ1pedc | 1 s，1 ms × 4 | 8 | 約 75 → 70* | 約 87 → 88* | 無效果 |
| 正對照（5H） | TH-GAL4 | γ1pedc | 1 s，1 ms × 4 | 5 | 約 98 → 14* | 約 100 → 82* | CS+、CS− 皆顯著 |
| 鄰區 MBON（5L） | MB320C | γ2α′1 | 1 s，1 ms × 4 | 6 | 約 105 → 91* | 約 89 → 92* | 無效果 |
| α2，短協定（6D） | MB099C | α2sc | 1 s，1 ms × 4 | 7 | 約 84 → 76* | 約 72 → 72* | 無效果 |
| α2，長協定（6H） | MB099C | α2sc | 60 s，1 ms × 120 | 6 | 約 74 → 5* | 約 66 → 58* | 只有 CS+ 顯著 |
| 以 PA 配對（7E） | MB320C | γ1pedc | 1 s，1 ms × 1 | 7 | PA 約 105 → 17* | BA 約 105 → 28；HP 約 92 → 30；EL 約 88 → 72* | PA、BA、HP 顯著 |
| 以 EL 配對（7H） | MB320C | γ1pedc | 1 s，1 ms × 1 | 5 | EL 約 83 → 20* | PA 約 100 → 72；BA 約 98 → 75；HP 約 83 → 53* | EL、HP 顯著 |
| **參照列：KC 層級（2E）** | MB320C | —（以鈣影像量 KC 細胞體） | 1 s，1 ms × 4 | 5 隻果蠅，有反應的 KC 細胞 OCT 53 顆、MCH 49 顆；不給光對照 2 隻果蠅 32 顆 | 小幅下降（ΔF/F，論文未給數值） | 小幅下降 | 三組（含不給光的對照）同樣下降 → 與配對無關 |

> 單位：未註明者為尖峰數（氣味開始後 0–1.4 s），pC 為 EPSC 電荷轉移。正向協定的 1 ms × 4 指四個 1 ms 光脈衝；「電壓箝制下配對」一列的 83% 是配對期間被壓掉的尖峰比例（用來檢驗 LTD 是否需要 MBON 放電，見 3.4）。圖 7 兩列的「未配對氣味」有三種，分別列出。標 * 者為本頁從圖上長條判讀的近似值，誤差約 ±5 spikes 或 ±20 pC；未標者為論文正文或圖說明列的數值。**最後一列是本頁補上的參照**：論文把 KC 的結果放在另一張圖（3.2）。並列之後可以看到，MBON 層級 CS+ 下降 80–90% 的同時，KC 細胞體只有小幅下降，而且不給光的對照組也同樣下降，表示那是成像本身造成的，不是配對造成的。KC 沒有配對專屬的改變、MBON 卻大幅下降，這是「改變發生在 KC 與 MBON 之間」這個推論的依據。另一個並列後才看得出的事實：**同一對氣味（OCT 為 CS+、MCH 為 CS−）在 γ1pedc 做了四次，CS− 有三次顯著下降（1F、4E／4H、5H）、一次不顯著（3D）**；四氣味實驗中，CS− 是否顯著也隨氣味而異（7E：BA、HP 顯著，EL 不顯著；7H：HP 顯著，PA、BA 不顯著）。CS− 的部分下降是常態，顯著與否與各實驗的 n 和協定有關，不是一個穩定的「專一／不專一」二分。

### 四、討論

**主張一：MB 輸出端存在由多巴胺誘發的異突觸 LTD，且它實現了聯想學習的最低邏輯要求。** 證據強。γ1pedc 的 CS+ 抑制在七張圖中反覆出現、幅度大（80–90%）、個別果蠅方向一致，且有不帶驅動品系的對照（圖 S5：除了沒有驅動品系、其餘基因型相同的果蠅，做同樣的氣味–光配對，氣味反應不變，表示抑制確實來自 CsChrimson 對 DAN 的活化；圖本身 ？待查）與 KC 層級的對照。**但「時間先後」只有兩個點**（見 3.1），「sub-second precision」是超出資料的措辭。「長期」在此指至少 40 分鐘（圖 S4，？待查），本篇沒有測更長的時間點，不能直接等同於行為上持續數小時以上的記憶。

**主張二：MBON 的價值編碼與 LTD 的方向相符。** MBON-γ1pedc 被光遺傳活化時引發趨近（Aso et al. 2014b），也就是它的活動推動果蠅「靠近」。學會躲避某個氣味後，這個推動靠近的訊號對該氣味就應該變弱，果蠅才會不再靠近——本篇看到的正是 CS+ 反應下降。這是一個簡潔的統一解釋，**論證的強度取決於 Aso 2014b 的價值分類**，本篇沒有自己檢驗 MBON-γ1pedc 的行為效果。

**主張三：區室各自獨立，多巴胺及其下游訊號不越界。** 證據中等。兩個方向的陰性結果都成立，但都是「n = 6–8、只測一種協定」的陰性結果，且有 3.5 節提到的替代解釋（鄰區門檻可能不同）。作者引用 Boto et al. 2014 的兩項觀察：(1) 熱遺傳活化 DAN 時，KC 軸突的 cAMP 只在該 DAN 支配的區室升高，這與本篇的區室專一一致；(2) 同一篇的鈣反應變化，在空間上與 cAMP 升高的區室並不吻合（有的區室 cAMP 升高但鈣反應不變，有的反過來）。作者承認第 (2) 點尚待解釋。

**主張四：不同區室的誘發規則不同。** 證據中等偏弱，理由見 3.6：協定同時改變兩個變數，驅動品系不同。作者的解釋是：行為文獻顯示 γ1pedc 在嫌惡記憶的「獲得」（形成記憶）中特別重要，一次短暫的懲罰就該留下記錄，所以它對多巴胺高度敏感；α2 則被認為較多參與記憶的「提取」（日後讀出記憶；Séjourné et al. 2011；Bouzaiane et al. 2015），不需要對單次刺激那麼敏感。這是引文獻的解釋，本篇沒有檢驗。

**主張五：稀疏編碼下的重疊決定可塑性的專一性與記憶的類化。** 證據中等。生理上的相關成立，但 r = 0.90 部分來自兩個定義上的自身點（見 3.7）；行為上的類化成立，但與生理是不同果蠅、不同協定。**「類化是由突觸干擾所介導」是對應關係，不是因果證明**。

**主張六：可塑性不需要 MBON 放電，只取決於 KC 與 DAN 的共同活動。** 證據強：圖 3 用 QX-314 讓 MBON 完全不能放電，圖 4 在配對時把尖峰壓掉 83%，兩者都仍出現同樣的 LTD。這與蝗蟲的 Hebbian STDP（Cassenaer & Laurent 2007）形成對比：在蝗蟲，突觸是否改變取決於 MBON 自己有沒有、何時放電；在果蠅，MBON 放不放電都不影響，決定因素是 KC 活動時有沒有多巴胺。作者由此提出一個簡單模型：多巴胺到達時（或稍早）活躍的 KC–MBON 突觸會被改變。**「稍早」的時間窗有多寬，本篇沒有量。**

### 五、問題與限制

**1. 時間規則只有兩個取樣點。** 一個正向（第一下光在氣味開始後 0.2 s）、一個反向（最後一下光在氣味開始前 0.5 s）。摘要的「strictly depends on the temporal order」與討論的「sub-second precision」都超出這兩點能支持的範圍。反向協定只看到「無變化」，沒有看到「增強」。（反向配對是否會產生與正向相反方向的改變，是時序規則的關鍵問題之一；本篇的資料不能回答。）

**2. 電生理與行為在不同果蠅上做。** 圖 7 的類化、圖 S1 的光遺傳學習都是另一批果蠅、不同的光協定。論文首頁的「In Brief」摘要框說作者「prove the long-standing hypothesis」，但沒有「阻斷這個 LTD 就阻斷學習」的實驗。

**3. 突觸前 vs 突觸後未定。** 作者排除了 KC 整體反應與興奮性的改變，沒有直接量 γ1 區的突觸前釋放或突觸後受器。討論中承認 Boto et al. 2014 在 γ1 軸突看不到鈣變化，並列出三種可能，未裁定：(a) 可塑性的分子機制位於鈣進入末梢之後的步驟，所以鈣訊號照常、釋放卻變少；(b) 鈣的變化太小、太局部，用散布在整個細胞質中的鈣指示劑偵測不到；(c) 改變主要發生在突觸後的 MBON 那一側，KC 末梢本來就沒有變。

**4. 其他突觸前元件。** 作者自陳：除了 KC 之外，其他把訊號送到 MBON 的神經元（例如 DPM 神經元）可能也有貢獻。

**5. 區室比較的混淆因子。** α2 vs γ1 用不同驅動品系（MB099C 依本篇為四型 DAN、依 Aso 2016 為兩型，見 [[syn-contradictions]] 1.4；vs MB320C 一型），協定同時改變氣味時長與光脈衝數。

**6. 只測一個方向的突觸改變。** 全篇只看到抑制，從未看到增強；但活化的都是 PPL1 群 DAN（TH-GAL4 那組另含少數 PAM 群 DAN），以 PPL1-γ1pedc 為主，也就是本篇引用的嫌惡學習路徑。論文引言提到，負責獎賞記憶與嫌惡記憶的 DAN 投射到 MB 葉的不同部位（Perisse et al. 2013）；獎賞那一類 DAN 誘發的可塑性方向，本篇沒有測。

**7. 依賴未取得的補充資料。** 「至少持續 40 分鐘」（圖 S4）、無驅動品系對照（圖 S5）、KC 興奮性（圖 S7）、光遺傳行為（圖 S1）、DAN 放電可靠度（圖 S2）、反轉 CS+／CS−（圖 S3）、γ1 的 1 分鐘協定與單脈衝協定（圖 S6）皆在補充資料中。本頁對這些的轉述只限於正文所說，細節 ？待查（補充資料未取得）。

**8.（本頁稽核）抑制只作用在持續段，起始暫態被保留，而論文沒有提到。**

- **現象**：圖 1E、3B–C、6G、7D 的配對後 CS+ 曲線，開頭都還有一個尖峰（放電約 50 spikes/s；EPSC 峰值約為配對前的八、九成；※ 從圖判讀），之後的持續反應才幾乎消失。論文描述圖 3 時卻寫電流「dramatically reduced early in the response」（反應早期就大幅降低）；圖上最開頭約 0.1–0.2 秒內的峰值仍在，大幅降低是從峰值之後開始（※ 從圖判讀）。原文的「early」也可能指峰值之後不久，有歧義。全文搜尋 transient／peak／initial／early 均未見對起始峰的討論。
- **為什麼重要之一**：「EPSC 降約九成」是電荷（整段時間的積分）的降幅，主要來自持續段消失。若下游神經元讀的主要是起始峰，MBON 輸出實際被削弱的程度遠小於九成。
- **為什麼重要之二**：作者的模型是「多巴胺到達時正在活動的突觸才會被削弱」。起始峰被保留，可能正是因為氣味剛開始時只短暫放電的 KC，在第一下光（0.2 s）之前就停了（見 3.3 的三種可能）。若是如此，起始峰就是這個模型「時間窗有多寬」的直接線索，而本篇沒有分析。
- 這不推翻 LTD 的存在。

**本頁另發現三處論文自身的不一致**（皆不影響主要結論）：CS− 的突觸電荷在圖 3 不顯著、在圖 4 顯著（3.4）；圖 2 圖說的 A–D 字母與圖面配置不符（3.2）；圖 7I 的 r = 0.90 含兩個定義上的自身點，去掉後約 0.85、p ≈ 0.03（3.7）。

### 六、未來

**論文自陳的方向。** (1) 突觸可塑性與 KC 軸突鈣訊號之間的落差「需要進一步研究」；(2) α2 的 PPL1-α′2α2 在其他刺激條件下可能誘發不同形式的可塑性；(3) 稀疏編碼（每種刺激只活化少數細胞）被下游讀出的方式，「可能廣泛適用於其他與記憶有關的腦區」。

**本庫關注的後續。** 本庫另兩篇與本篇的對照如下：
- **時間窗**：[[s-handler-2019-dopamine-receptor-timing]] 補上了本篇只有兩個取樣點的時間規則（「五、問題與限制」第 1 條），但是在另一個區室（γ4）、取出的腦、另一群多巴胺神經元（PAM）上做的：多巴胺早 1.2 秒，突觸變強；同時或晚 0.5 秒，變弱；相差 6 秒，幾乎不變。本篇的逆向配對（光比氣味早 2.0 到 0.5 秒）則完全無效。兩篇對「逆向配對是無效還是反向」說法不同，本庫列為待裁決，見 [[syn-contradictions]] 1.1。
- **受體與第二傳訊者**：Handler 2019 指出 DopR1 製造的 cAMP 推動突觸變弱，回答了本篇「由哪種受器介導」的一半（「尚未被回答的」第 2 項），但它量的也是輸出神經元的反應，**突觸前還是突觸後**仍沒有人直接量。該篇引用本篇，作為「順向配對造成減弱」與「同一條 KC 軸突上不同區室的突觸可以各自調整」的依據。
- **突觸前端**：[[s-tomchik-2009-camp-dynamics]] 在取出的腦裡看到，乙醯膽鹼（模擬氣味）與多巴胺順向配對時，KC 軸突的 cAMP 上升超過兩者分開給的總和，與本篇「KC 與 DAN 共同活動決定可塑性」的模型相容。但該篇也發現用藥物拉高 cAMP 會讓 KC 內的鈣反應**增強**，與本篇的輸出**減弱**看似方向相反，見 [[syn-contradictions]] 3.2。
- **區室門檻**：本篇 α2 與 γ1 的門檻差異，在另兩篇都沒有對應資料；Handler 2019 的受體實驗只在 γ4/γ5（[[syn-contradictions]] 3.4）。
- 兩條主題頁把本篇與相關來源並排：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]。

**尚未被回答的。** (1) 正向與反向之間的完整時間窗形狀；(2) LTD 在突觸前還是突觸後表現，由哪種受器與第二傳訊者介導（本篇沒有操作任何受器或第二傳訊者）；(3) 負責獎賞學習的 DAN 在其區室誘發的可塑性方向；(4) 起始暫態為何不受抑制；(5) 阻斷 γ1pedc 的 LTD 是否足以阻斷嫌惡學習或類化；(6) 「長期」能否延伸到小時或天。

---

## 相關

- [[numbers]] — 本篇貢獻 MBON-γ1pedc 的 LTD 幅度（尖峰 −80%、電荷 −90%）、CS− 的部分抑制（27% vs 20%）、KC 重疊（30%／33%）、類化相關 r = 0.90、各實驗 n 與協定參數
- 本庫已有的相關頁：[[e-mushroom-body]]、[[e-kenyon-cell]]、[[e-split-gal4]]、[[e-cschrimson]]、[[e-gcamp]]、[[c-kc-mbon-plasticity]]、[[c-mb-compartment]]、[[c-cs-us-timing]]、[[c-us-substitution]]、[[c-performance-index]]、[[e-dopaminergic-neuron]]、[[e-mbon]]
- 主題：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]；矛盾與空缺：[[syn-contradictions]]
- 主題：[[t-stereotypy-to-individualization]]（本篇是該線唯一同時量到「KC 的代碼沒動、MBON 的輸入降約九成」的一篇；其引言也是庫內確認 Hige 2015 *Nature* 個體化那篇出處的來源）
- 本批（2026-10-25 第二批）已開頁、與本篇相關：[[e-mbon-gamma1pedc]]、[[e-ppl1-gamma1pedc]]、[[e-mbon-gamma2alpha1]]、[[e-mb099c]]、[[e-th-gal4]]、[[c-odor-generalization]]、[[c-whole-cell-patch-clamp]]
- 概念：[[c-sparse-coding]]（本篇與 [[s-minnick-2026-untrained-connectome]] 使它在 2026-11-12 達到開頁門檻）
- 實體：[[e-mbon-alpha2sc]]、[[e-ppl1-alpha2alpha2]]（因 [[s-huang-2024-dopamine-memory-dynamics]] 在 2026-11-13 達到開頁門檻）
- 2026-11-13 第一批整合時補上的連結 — 正文提到、相關節原本漏列的來源：[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]
- 待開頁面：`e-campbell-2013-odor-set`、`c-synaptic-interference`、[[c-valence-coding]]

## 出處

Hige, T., Aso, Y., Modi, M. N., Rubin, G. M., & Turner, G. C. (2015). Heterosynaptic plasticity underlies aversive olfactory learning in *Drosophila*. *Neuron*, 88(5), 985–998. https://doi.org/10.1016/j.neuron.2015.11.003

圖片擷取自原文，版權屬原出版社（© 2015 Elsevier Inc.），本庫以教學與評論目的引用，不代表出版社授權。全文請至 https://pmc.ncbi.nlm.nih.gov/articles/PMC4674068/ 免費閱讀。
