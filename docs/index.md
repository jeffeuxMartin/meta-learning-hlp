<h1 id="meta-learning-for-human-language-processing">(Adjusting) Meta learning for human language processing</h1>
<table>
	<thead>
		<tr>
			<th></th>
			<th>(A) <strong>Learning to initialize</strong></th>
			<th>(B) <strong>Learning to compare</strong></th>
			<th>(C) <strong>Other</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Text Classification</td>
			<td><span id="back__Dou__COLON__EMNLP19">(<a href="#Dou__COLON__EMNLP19">Dou et al., EMNLP’19</a>)</span>
				<br /> <span id="back__Bansal__COLON__arXiv19">(<a href="#Bansal__COLON__arXiv19">Bansal et al.,
						arXiv’19</a>)</span> <br /> <span id="back__holla__DASH__etal__DASH__2020__DASH__learning">(<a
						href="#holla__DASH__etal__DASH__2020__DASH__learning">Holla et al., Findings of
						EMNLP’20</a>)</span> <br /> <span id="back__MetaKD__DASH__arXiv21">(<a
						href="#MetaKD__DASH__arXiv21">Zhou et al., arXiv’21</a>)</span> <br /> <span
					id="back__van__DASH__der__DASH__heijden__DASH__etal__DASH__2021__DASH__multilingual">(<a
						href="#van__DASH__der__DASH__heijden__DASH__etal__DASH__2021__DASH__multilingual">van der
						Heijden et al., EACL’21</a>)</span> <br /> <span
					id="back__bansal__DASH__etal__DASH__2020__DASH__self">(<a
						href="#bansal__DASH__etal__DASH__2020__DASH__self">Bansal et al., EMNLP’20</a>)</span> <br />
				<span id="back__murty__DASH__etal__DASH__2021__DASH__dreca">(<a
						href="#murty__DASH__etal__DASH__2021__DASH__dreca">Murty et al., NAACL’21</a>)</span></td>
			<td><span id="back__Yu__COLON__ACL18">(<a href="#Yu__COLON__ACL18">Yu et al., ACL’18</a>)</span> <br />
				<span id="back__Tan__COLON__EMNLP19">(<a href="#Tan__COLON__EMNLP19">Tan et al., EMNLP’19</a>)</span>
				<br /> <span id="back__Geng__COLON__EMNLP19">(<a href="#Geng__COLON__EMNLP19">Geng et al.,
						EMNLP’19</a>)</span> <br /> <span id="back__Sun__COLON__EMNLP19">(<a
						href="#Sun__COLON__EMNLP19">Sun et al., EMNLP’19</a>)</span> <br /> <span
					id="back__geng2020dynamic">(<a href="#geng2020dynamic">Geng et al., ACL’20</a>)</span></td>
			<td>Learning the learning algorithm: <br /> <span id="back__Wu__COLON__EMNLP19">(<a
						href="#Wu__COLON__EMNLP19">Wu et al., EMNLP’19</a>)</span> <br /> Network architecture search:
				<br /> <span id="back__pasunuru2020fenas">(<a href="#pasunuru2020fenas">Pasunuru and Bansal,
						EMNLP’20</a>)</span> <br /> <span id="back__pasunuru2019continual">(<a
						href="#pasunuru2019continual">Pasunuru and Bansal, ACL’19</a>)</span> <br /> Learning to
				optimize: <br /> <span id="back__learningToOptimize__COLON__metaNLP21">(<a
						href="#learningToOptimize__COLON__metaNLP21">Xu et al., MetaNLP’21a</a>)</span> <br /> Learning
				to select data: <br /> <span id="back__label__DASH__correction__DASH__aaai21">(<a
						href="#label__DASH__correction__DASH__aaai21">Zheng et al., AAAI’21</a>)</span></td>
		</tr>
		<tr>
			<td>Sequence Labelng</td>
			<td><span id="back__Wu__COLON__AAAI20">(<a href="#Wu__COLON__AAAI20">Wu et al., AAAI’20</a>)</span> <br />
				<span id="back__xia__DASH__etal__DASH__2021__DASH__metaxl">(<a
						href="#xia__DASH__etal__DASH__2021__DASH__metaxl">Xia et al., NAACL’21</a>)</span></td>
			<td><span id="back__Hou__COLON__ACL20">(<a href="#Hou__COLON__ACL20">Hou et al., ACL’20</a>)</span> <br />
				<span id="back__yang2020frustratingly">(<a href="#yang2020frustratingly">Yi and Katiyar,
						EMNLP’20</a>)</span> <br /> <span id="back__oguz2021few">(<a href="#oguz2021few">Oguz and Vu,
						EACL’21</a>)</span></td>
			<td>Network architecture search: <br /> <span id="back__li2020learning">(<a href="#li2020learning">Li et
						al., ACL’20</a>)</span> <br /> <span id="back__jiang2019improved">(<a
						href="#jiang2019improved">Jiang et al., EMNLP’19</a>)</span></td>
		</tr>
		<tr>
			<td>Relation Classification</td>
			<td><span id="back__Obamuyide__COLON__ACL19">(<a href="#Obamuyide__COLON__ACL19">Obamuyide and Vlachos,
						ACL’19</a>)</span> <br /> <span id="back__Bose__COLON__arXiv19">(<a
						href="#Bose__COLON__arXiv19">Bose et al., arXiv’19</a>)</span> <br /> <span
					id="back__Lv__COLON__EMNLP19">(<a href="#Lv__COLON__EMNLP19">Lv et al., EMNLP’19</a>)</span></td>
			<td><span id="back__Ye__COLON__ACL19">(<a href="#Ye__COLON__ACL19">Ye and Ling, ACL’19</a>)</span> <br />
				<span id="back__Chen__COLON__EMNLP19">(<a href="#Chen__COLON__EMNLP19">Chen et al., EMNLP’19</a>)</span>
				<br /> <span id="back__Xiong__COLON__EMNLP18">(<a href="#Xiong__COLON__EMNLP18">Xiong et al.,
						EMNLP’18a</a>)</span> <br /> <span id="back__Gao__COLON__AAAI19">(<a
						href="#Gao__COLON__AAAI19">Gao et al., AAAI’19</a>)</span> <br /> <span
					id="back__ren2020two">(<a href="#ren2020two">Ren et al., COLING’20</a>)</span></td>
			<td></td>
		</tr>
		<tr>
			<td>Knowledge Graph Completion</td>
			<td></td>
			<td><span id="back__xiong2018one">(<a href="#xiong2018one">Xiong et al., EMNLP’18b</a>)</span> <br /> <span
					id="back__wang2019tackling">(<a href="#wang2019tackling">Wang et al., EMNLP-IJCNLP’19</a>)</span>
				<br /> <span id="back__zhang2020few">(<a href="#zhang2020few">Zhang et al., AAAI’20</a>)</span> <br />
				<span id="back__sheng2020adaptive">(<a href="#sheng2020adaptive">Sheng et al., EMNLP’20</a>)</span></td>
			<td></td>
		</tr>
		<tr>
			<td>Word Embedding</td>
			<td><span id="back__Hu__COLON__ACL19">(<a href="#Hu__COLON__ACL19">Hu et al., ACL’19</a>)</span></td>
			<td><span id="back__Sun__COLON__EMNLP18">(<a href="#Sun__COLON__EMNLP18">Sun et al., EMNLP’18</a>)</span>
			</td>
			<td>Network architecture search: <br /> <span id="back__li2020learning">(<a href="#li2020learning">Li et
						al., ACL’20</a>)</span> <br /> <span id="back__jiang2019improved">(<a
						href="#jiang2019improved">Jiang et al., EMNLP’19</a>)</span></td>
		</tr>
		<tr>
			<td>Question Answering</td>
			<td><span id="back__mhamdi__DASH__etal__DASH__2021__DASH__x">(<a
						href="#mhamdi__DASH__etal__DASH__2021__DASH__x">M&#39;hamdi et al., NAACL’21</a>)</span> <br />
				<span id="back__nooralahzadeh__DASH__etal__DASH__2020__DASH__zero">(<a
						href="#nooralahzadeh__DASH__etal__DASH__2020__DASH__zero">Nooralahzadeh et al.,
						EMNLP’20</a>)</span> <br /> <span
					id="back__yan__DASH__etal__DASH__2020__DASH__multi__DASH__source">(<a
						href="#yan__DASH__etal__DASH__2020__DASH__multi__DASH__source">Yan et al., ACL’20</a>)</span>
				<br /> <span id="back__hua__DASH__etal__DASH__2020__DASH__shot">(<a
						href="#hua__DASH__etal__DASH__2020__DASH__shot">Hua et al., EMNLP’20</a>)</span></td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td>Machine Translation</td>
			<td><span id="back__Gu__COLON__EMNLP18">(<a href="#Gu__COLON__EMNLP18">Gu et al., EMNLP’18</a>)</span>
				<br /> <span id="back__Indurthi__COLON__arXiv19">(<a href="#Indurthi__COLON__arXiv19">Indurthi et al.,
						ICASSP’20</a>)</span> <br /> <span id="back__Li_Wang_Yu_2020">(<a href="#Li_Wang_Yu_2020">Li et
						al., AAAI’20</a>)</span> <br /> <span id="back__unsupervisedMT__DASH__acl21">(<a
						href="#unsupervisedMT__DASH__acl21">Park et al., ACL’21</a>)</span></td>
			<td></td>
			<td>Network architecture search: <br /> <span id="back__wang2020hat">(<a href="#wang2020hat">Wang et al.,
						ACL’20a</a>)</span> <br /> Learning to select data: <br /> <span
					id="back__wang2020balancing">(<a href="#wang2020balancing">Wang et al., ACL’20b</a>)</span> <br />
				<span id="back__pham2020meta">(<a href="#pham2020meta">Pham et al., ICLR’21</a>)</span></td>
		</tr>
		<tr>
			<td>Parsing</td>
			<td><span id="back__Guo__COLON__ACL19">(<a href="#Guo__COLON__ACL19">Guo et al., ACL’19</a>)</span> <br />
				<span id="back__Huang__COLON__NAACL18">(<a href="#Huang__COLON__NAACL18">Huang et al.,
						NAACL’18</a>)</span> <br /> <span id="back__multiparsing">(<a href="#multiparsing">Langedijk et
						al., arXiv’21</a>)</span> <br /> <span id="back__chen__DASH__etal__DASH__2020__DASH__low">(<a
						href="#chen__DASH__etal__DASH__2020__DASH__low">Chen et al., EMNLP’20</a>)</span> <br /> <span
					id="back__wang__DASH__etal__DASH__2021__DASH__meta">(<a
						href="#wang__DASH__etal__DASH__2021__DASH__meta">Wang et al., NAACL’21</a>)</span></td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td>Dialogue</td>
			<td><span id="back__Qian__COLON__ACL19">(<a href="#Qian__COLON__ACL19">Qian et al., ACL’19</a>)</span>
				<br /> <span id="back__Madotto__COLON__ACL19">(<a href="#Madotto__COLON__ACL19">Madotto et al.,
						ACL’19</a>)</span> <br /> <span id="back__Mi__COLON__IJCAI19">(<a href="#Mi__COLON__IJCAI19">Mi
						et al., IJCAI’19</a>)</span> <br /> <span id="back__Huang__COLON__ACL20">(<a
						href="#Huang__COLON__ACL20">Huang et al., ACL’20</a>)</span> <br /> <span
					id="back__dingliwal__DASH__etal__DASH__2021__DASH__shot">(<a
						href="#dingliwal__DASH__etal__DASH__2021__DASH__shot">Dingliwal et al., EACL’21</a>)</span>
				<br /> <span id="back__ST__DASH__dialogue__DASH__AAAI21">(<a
						href="#ST__DASH__dialogue__DASH__AAAI21">Qian et al., AAAI’21</a>)</span> <br /> <span
					id="back__dai__DASH__etal__DASH__2020__DASH__learning">(<a
						href="#dai__DASH__etal__DASH__2020__DASH__learning">Dai et al., ACL’20</a>)</span> <br /> <span
					id="back__huang__DASH__etal__DASH__2020__DASH__towards__DASH__low">(<a
						href="#huang__DASH__etal__DASH__2020__DASH__towards__DASH__low">Huang et al., Findings of
						EMNLP’20</a>)</span></td>
			<td></td>
			<td>Learning to optimize: <br /> <span id="back__Chien__COLON__INTERSPEECH19">(<a
						href="#Chien__COLON__INTERSPEECH19">Chien and Lieow, INTERSPEECH’19</a>)</span></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td>Speech Recognition</td>
			<td><span id="back__Hsu__COLON__ICASSP20">(<a href="#Hsu__COLON__ICASSP20">Hsu et al., ICASSP’20</a>)</span>
				<br /> <span id="back__Klejch__COLON__ASRU19">(<a href="#Klejch__COLON__ASRU19">Klejch et al.,
						ASRU’19</a>)</span> <br /> <span id="back__Winata__COLON__ACL2020">(<a
						href="#Winata__COLON__ACL2020">Winata et al., ACL’20</a>)</span> <br /> <span
					id="back__Winata__COLON__INTERSPEECH2020">(<a href="#Winata__COLON__INTERSPEECH2020">Winata et al.,
						INTERSPEECH’20</a>)</span> <br /> <span id="back__ASR__DASH__sample__DASH__AAAI21">(<a
						href="#ASR__DASH__sample__DASH__AAAI21">Xiao et al., AAAI’21</a>)</span></td>
			<td><span id="back__lux2021meta">(<a href="#lux2021meta">Lux et al., ICASSP’21</a>)</span></td>
			<td>Learning to optimize: <br /> <span id="back__Klejch__COLON__INTERSPEECH18">(<a
						href="#Klejch__COLON__INTERSPEECH18">Klejch et al., INTERSPEECH’18</a>)</span> <br /> Network
				architecture search: <br /> <span id="back__Chen__COLON__INTERSPEECH20">(<a
						href="#Chen__COLON__INTERSPEECH20">Chen et al., INTERSPEECH’20a</a>)</span> <br /> <span
					id="back__Baruwa__COLON__IJSER19">(<a href="#Baruwa__COLON__IJSER19">Baruwa et al.,
						IJSER’19</a>)</span></td>
		</tr>
		<tr>
			<td>Source Separation</td>
			<td><span id="back__SP__DASH__ICASSP21">(<a href="#SP__DASH__ICASSP21">Wu et al., ICASSP’21</a>)</span>
				<br /> <span id="back__Huang__DASH__ACLMeta">(<a href="#Huang__DASH__ACLMeta">Huang et al.,
						MetaNLP’21</a>)</span></td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td>Keyword Spotting</td>
			<td><span id="back__Chen__COLON__arXiv18">(<a href="#Chen__COLON__arXiv18">Chen et al.,
						INTERSPEECH’20b</a>)</span></td>
			<td></td>
			<td>Network architecture search: <br /> <span id="back__Mazzawi__COLON__INTERSPEECH19">(<a
						href="#Mazzawi__COLON__INTERSPEECH19">Mazzawi et al., INTERSPEECH’19</a>)</span></td>
		</tr>
		<tr>
			<td>Sound Event Detection</td>
			<td></td>
			<td><span id="back__Shimada__COLON__arXiv19">(<a href="#Shimada__COLON__arXiv19">Shimada et al.,
						ICASSP’20</a>)</span> <br /> <span id="back__Chou__COLON__ICASSP19">(<a
						href="#Chou__COLON__ICASSP19">Chou et al., ICASSP’19</a>)</span></td>
			<td></td>
		</tr>
		<tr>
			<td>Voice Cloning</td>
			<td></td>
			<td></td>
			<td>Learning the learning algorithm: <br /> <span id="back__Chen__COLON__ICLR19">(<a
						href="#Chen__COLON__ICLR19">Chen et al., ICLR’19</a>)</span> <br /> <span
					id="back__Serra__COLON__NeurIPS19">(<a href="#Serra__COLON__NeurIPS19">Serrà et al.,
						NeurIPS’19</a>)</span></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td>Multi-tasks</td>
			<td></td>
			<td></td>
			<td>Learning to select data: <br /> <span id="back__tarunesh2021meta">(<a href="#tarunesh2021meta">Tarunesh
						et al., EACL’21</a>)</span></td>
		</tr>
		<tr>
			<td>Multi-modal</td>
			<td></td>
			<td><span id="back__Eloff__COLON__ICASSP19">(<a href="#Eloff__COLON__ICASSP19">Eloff et al.,
						ICASSP’19</a>)</span></td>
			<td>Learning the learning algorithm: <br /> <span id="back__Suris__COLON__arXiv19">(<a
						href="#Suris__COLON__arXiv19">Surís et al., arXiv’19</a>)</span> <br /> <span
					id="back__learningToLearn__COLON__metaNLP21">(<a href="#learningToLearn__COLON__metaNLP21">Xu et
						al., MetaNLP’21b</a>)</span></td>
		</tr>
	</tbody>
</table>
<ul>
	<li><span id="bansal__DASH__etal__DASH__2020__DASH__self"> [<a
				href="#back__bansal__DASH__etal__DASH__2020__DASH__self">Bansal et al., EMNLP’20</a>] <i>Bansal, Trapit
				and Jha, Rishikesh and Munkhdalai, Tsendsuren and McCallum, Andrew</i>, Self-Supervised Meta-Learning
			for Few-Shot Natural Language Classification Tasks, EMNLP, 2020</span></li>
	<li><span id="Bansal__COLON__arXiv19"> [<a href="#back__Bansal__COLON__arXiv19">Bansal et al., arXiv’19</a>]
			<i>Trapit Bansal and Rishikesh Jha and Andrew McCallum</i>, Learning to Few-Shot Learn Across Diverse
			Natural Language Classification Tasks, arXiv, 2019 <a
				href="https://aclanthology.org/2020.coling-main.448.pdf">:link:</a></span></li>
	<li><span id="Baruwa__COLON__IJSER19"> [<a href="#back__Baruwa__COLON__IJSER19">Baruwa et al., IJSER’19</a>]
			<i>Ahmed Baruwa and Mojeed Abisiga and Ibrahim Gbadegesin and Afeez Fakunle</i>, Leveraging End-to-End
			Speech Recognition with Neural Architecture Search, IJSER, 2019</span></li>
	<li><span id="Bose__COLON__arXiv19"> [<a href="#back__Bose__COLON__arXiv19">Bose et al., arXiv’19</a>] <i>Avishek
				Joey Bose and Ankit Jain and Piero Molino and William L. Hamilton</i>, Meta-Graph:Few shot Link
			Prediction via Meta Learning, arXiv, 2019</span></li>
	<li><span id="Chen__COLON__EMNLP19"> [<a href="#back__Chen__COLON__EMNLP19">Chen et al., EMNLP’19</a>] <i>Mingyang
				Chen and Wen Zhang and Wei Zhang and Qiang Chen and Huajun Chen</i>, Meta Relational Learning for
			Few-Shot Link Prediction in Knowledge Graphs, EMNLP, 2019</span></li>
	<li><span id="chen__DASH__etal__DASH__2020__DASH__low"> [<a
				href="#back__chen__DASH__etal__DASH__2020__DASH__low">Chen et al., EMNLP’20</a>] <i>Chen, Xilun and
				Ghoshal, Asish and Mehdad, Yashar and Zettlemoyer, Luke and Gupta, Sonal</i>, Low-Resource Domain
			Adaptation for Compositional Task-Oriented Semantic Parsing, EMNLP, 2020</span></li>
	<li><span id="Chen__COLON__ICLR19"> [<a href="#back__Chen__COLON__ICLR19">Chen et al., ICLR’19</a>] <i>Yutian Chen
				and Yannis Assael and Brendan Shillingford and David Budden and Scott Reed and Heiga Zen and Quan Wang
				and Luis C. Cobo and Andrew Trask and Ben Laurie and Caglar Gulcehre and Aäron van den Oord and Oriol
				Vinyals and Nando de Freitas</i>, Sample Efficient Adaptive Text-to-Speech, ICLR, 2019</span></li>
	<li><span id="Chen__COLON__INTERSPEECH20"> [<a href="#back__Chen__COLON__INTERSPEECH20">Chen et al.,
				INTERSPEECH’20a</a>] <i>Yi-Chen Chen and Jui-Yang Hsu and Cheng-Kuang Lee and Hung-yi Lee</i>,
			DARTS-ASR: Differentiable Architecture Search for Multilingual Speech Recognition and Adaptation,
			INTERSPEECH, 2020</span></li>
	<li><span id="Chen__COLON__arXiv18"> [<a href="#back__Chen__COLON__arXiv18">Chen et al., INTERSPEECH’20b</a>]
			<i>Yangbin Chen and Tom Ko and Lifeng Shang and Xiao Chen and Xin Jiang and Qing Li</i>, An Investigation of
			Few-Shot Learning in Spoken Term Classification, INTERSPEECH, 2020</span></li>
	<li><span id="Chien__COLON__INTERSPEECH19"> [<a href="#back__Chien__COLON__INTERSPEECH19">Chien and Lieow,
				INTERSPEECH’19</a>] <i>Jen-Tzung Chien and Wei Xiang Lieow</i>, Meta Learning for Hyperparameter
			Optimization in Dialogue System, INTERSPEECH, 2019</span></li>
	<li><span id="Chou__COLON__ICASSP19"> [<a href="#back__Chou__COLON__ICASSP19">Chou et al., ICASSP’19</a>] <i>Szu-Yu
				Chou and Kai-Hsiang Cheng and Jyh-Shing Roger Jang and Yi-Hsuan Yang</i>, Learning to match transient
			sound events using attentional similarity for few-shot sound recognition, ICASSP, 2019</span></li>
	<li><span id="dai__DASH__etal__DASH__2020__DASH__learning"> [<a
				href="#back__dai__DASH__etal__DASH__2020__DASH__learning">Dai et al., ACL’20</a>] <i>Dai, Yinpei and Li,
				Hangyu and Tang, Chengguang and Li, Yongbin and Sun, Jian and Zhu, Xiaodan</i>, Learning Low-Resource
			End-To-End Goal-Oriented Dialog for Fast and Reliable System Deployment, ACL, 2020</span></li>
	<li><span id="dingliwal__DASH__etal__DASH__2021__DASH__shot"> [<a
				href="#back__dingliwal__DASH__etal__DASH__2021__DASH__shot">Dingliwal et al., EACL’21</a>] <i>Dingliwal,
				Saket and Gao, Shuyang and Agarwal, Sanchit and Lin, Chien-Wei and Chung, Tagyoung and Hakkani-Tur,
				Dilek</i>, Few Shot Dialogue State Tracking using Meta-learning, EACL, 2021</span></li>
	<li><span id="Dou__COLON__EMNLP19"> [<a href="#back__Dou__COLON__EMNLP19">Dou et al., EMNLP’19</a>] <i>Zi-Yi Dou and
				Keyi Yu and Antonios Anastasopoulos</i>, Investigating Meta-Learning Algorithms for Low-Resource Natural
			Language Understanding Tasks, EMNLP, 2019</span></li>
	<li><span id="Eloff__COLON__ICASSP19"> [<a href="#back__Eloff__COLON__ICASSP19">Eloff et al., ICASSP’19</a>] <i>Ryan
				Eloff and Herman A. Engelbrecht and Herman Kamper</i>, MULTIMODAL ONE-SHOT LEARNING OF SPEECH AND
			IMAGES, ICASSP, 2019</span></li>
	<li><span id="Gao__COLON__AAAI19"> [<a href="#back__Gao__COLON__AAAI19">Gao et al., AAAI’19</a>] <i>Tianyu Gao and
				Xu Han and Zhiyuan Liu and Maosong Sun</i>, Hybrid Attention-Based Prototypical Networks for Noisy
			Few-Shot Relation Classification, AAAI, 2019</span></li>
	<li><span id="geng2020dynamic"> [<a href="#back__geng2020dynamic">Geng et al., ACL’20</a>] <i>Geng, Ruiying and Li,
				Binhua and Li, Yongbin and Sun, Jian and Zhu, Xiaodan</i>, Dynamic Memory Induction Networks for
			Few-Shot Text Classification, ACL, 2020</span></li>
	<li><span id="Geng__COLON__EMNLP19"> [<a href="#back__Geng__COLON__EMNLP19">Geng et al., EMNLP’19</a>] <i>Ruiying
				Geng and Binhua Li and Yongbin Li and Xiaodan Zhu and Ping Jian and Jian Sun</i>, Induction Networks for
			Few-Shot Text Classification, EMNLP, 2019</span></li>
	<li><span id="Gu__COLON__EMNLP18"> [<a href="#back__Gu__COLON__EMNLP18">Gu et al., EMNLP’18</a>] <i>Jiatao Gu and
				Yong Wang and Yun Chen and Kyunghyun Cho and Victor O.K. Li</i>, Meta-Learning for Low-Resource Neural
			Machine Translation, EMNLP, 2018</span></li>
	<li><span id="Guo__COLON__ACL19"> [<a href="#back__Guo__COLON__ACL19">Guo et al., ACL’19</a>] <i>Daya Guo and Duyu
				Tang and Nan Duan and Ming Zhou and Jian Yin</i>, Coupling Retrieval and Meta-Learning for
			Context-Dependent Semantic Parsing, ACL, 2019</span></li>
	<li><span id="holla__DASH__etal__DASH__2020__DASH__learning"> [<a
				href="#back__holla__DASH__etal__DASH__2020__DASH__learning">Holla et al., Findings of EMNLP’20</a>]
			<i>Holla, Nithin and Mishra, Pushkar and Yannakoudakis, Helen and Shutova, Ekaterina</i>, Learning to Learn
			to Disambiguate: Meta-Learning for Few-Shot Word Sense Disambiguation, Findings of EMNLP, 2020</span></li>
	<li><span id="Hou__COLON__ACL20"> [<a href="#back__Hou__COLON__ACL20">Hou et al., ACL’20</a>] <i>Yutai Hou and
				Wanxiang Che and Yongkui Lai and Zhihan Zhou and Yijia Liu and Han Liu and Ting Liu</i>, Few-shot Slot
			Tagging with Collapsed Dependency Transfer and Label-enhanced Task-adaptive Projection Network, ACL,
			2020</span></li>
	<li><span id="Hsu__COLON__ICASSP20"> [<a href="#back__Hsu__COLON__ICASSP20">Hsu et al., ICASSP’20</a>] <i>Jui-Yang
				Hsu and Yuan-Jui Chen and Hung-yi Lee</i>, Meta Learning for End-to-End Low-Resource Speech Recognition,
			ICASSP, 2020</span></li>
	<li><span id="Hu__COLON__ACL19"> [<a href="#back__Hu__COLON__ACL19">Hu et al., ACL’19</a>] <i>Ziniu Hu and Ting Chen
				and Kai-Wei Chang and Yizhou Sun</i>, Few-Shot Representation Learning for Out-Of-Vocabulary Words, ACL,
			2019</span></li>
	<li><span id="hua__DASH__etal__DASH__2020__DASH__shot"> [<a
				href="#back__hua__DASH__etal__DASH__2020__DASH__shot">Hua et al., EMNLP’20</a>] <i>Hua, Yuncheng and Li,
				Yuan-Fang and Haffari, Gholamreza and Qi, Guilin and Wu, Tongtong</i>, Few-Shot Complex Knowledge Base
			Question Answering via Meta Reinforcement Learning, EMNLP, 2020</span></li>
	<li><span id="Huang__COLON__ACL20"> [<a href="#back__Huang__COLON__ACL20">Huang et al., ACL’20</a>] <i>Yi Huang and
				Junlan Feng and Min Hu and Xiaoting Wu and Xiaoyu Du and Shuo Ma</i>, Meta-Reinforced Multi-Domain State
			Generator for Dialogue Systems, ACL, 2020</span></li>
	<li><span id="huang__DASH__etal__DASH__2020__DASH__towards__DASH__low"> [<a
				href="#back__huang__DASH__etal__DASH__2020__DASH__towards__DASH__low">Huang et al., Findings of
				EMNLP’20</a>] <i>Huang, Yi and Feng, Junlan and Ma, Shuo and Du, Xiaoyu and Wu, Xiaoting</i>, Towards
			Low-Resource Semi-Supervised Dialogue Generation with Meta-Learning, Findings of EMNLP, 2020</span></li>
	<li><span id="Huang__DASH__ACLMeta"> [<a href="#back__Huang__DASH__ACLMeta">Huang et al., MetaNLP’21</a>] <i>Kuan-Po
				Huang, Yuan-Kuei Wu, Hung-yi Lee</i>, Multi-accent Speech Separation with One Shot Learning, MetaNLP,
			2021 <a href="https://arxiv.org/pdf/2106.11713.pdf">:link:</a></span></li>
	<li><span id="Huang__COLON__NAACL18"> [<a href="#back__Huang__COLON__NAACL18">Huang et al., NAACL’18</a>] <i>Po-Sen
				Huang and Chenglong Wang and Rishabh Singh and Wen-tau Yih and Xiaodong He</i>, Natural Language to
			Structured Query Generation via Meta-Learning, NAACL, 2018</span></li>
	<li><span id="Indurthi__COLON__arXiv19"> [<a href="#back__Indurthi__COLON__arXiv19">Indurthi et al., ICASSP’20</a>]
			<i>Sathish Indurthi and Houjeung Han and Nikhil Kumar Lakumarapu and Beomseok Lee and Insoo Chung and Sangha
				Kim and Chanwoo Kim</i>, Data Efficient Direct Speech-to-Text Translation with Modality Agnostic
			Meta-Learning, ICASSP, 2020</span></li>
	<li><span id="jiang2019improved"> [<a href="#back__jiang2019improved">Jiang et al., EMNLP’19</a>] <i>Jiang, Yufan
				and Hu, Chi and Xiao, Tong and Zhang, Chunliang and Zhu, Jingbo</i>, Improved differentiable
			architecture search for language modeling and named entity recognition, EMNLP, 2019</span></li>
	<li><span id="Klejch__COLON__ASRU19"> [<a href="#back__Klejch__COLON__ASRU19">Klejch et al., ASRU’19</a>] <i>Ondřej
				Klejch and Joachim Fainberg and Peter Bell and Steve Renals</i>, Speaker Adaptive Training using Model
			Agnostic Meta-Learning, ASRU, 2019</span></li>
	<li><span id="Klejch__COLON__INTERSPEECH18"> [<a href="#back__Klejch__COLON__INTERSPEECH18">Klejch et al.,
				INTERSPEECH’18</a>] <i>Ondřej Klejch and Joachim Fainberg and Peter Bell</i>, Learning to adapt:a
			meta-learning approach for speaker adaptation, INTERSPEECH, 2018</span></li>
	<li><span id="multiparsing"> [<a href="#back__multiparsing">Langedijk et al., arXiv’21</a>] <i>Anna Langedijk and
				Verna Dankers and Phillip Lippe and Sander Bos and Bryan Cardenas Guevara and Helen Yannakoudakis and
				Ekaterina Shutova</i>, Meta-learning for fast cross-lingual adaptation in dependency parsing, arXiv,
			2021</span></li>
	<li><span id="Li_Wang_Yu_2020"> [<a href="#back__Li_Wang_Yu_2020">Li et al., AAAI’20</a>] <i>Li, Rumeng and Wang,
				Xun and Yu, Hong</i>, MetaMT, a Meta Learning Method Leveraging Multiple Domain Data for Low Resource
			Machine Translation, AAAI, 2020</span></li>
	<li><span id="li2020learning"> [<a href="#back__li2020learning">Li et al., ACL’20</a>] <i>Li, Yinqiao and Hu, Chi
				and Zhang, Yuhao and Xu, Nuo and Jiang, Yufan and Xiao, Tong and Zhu, Jingbo and Liu, Tongran and Li,
				Changliang</i>, Learning Architectures from an Extended Search Space for Language Modeling, ACL,
			2020</span></li>
	<li><span id="lux2021meta"> [<a href="#back__lux2021meta">Lux et al., ICASSP’21</a>] <i>Lux, Florian and Vu, Ngoc
				Thang</i>, Meta-Learning for improving rare word recognition in end-to-end ASR, ICASSP, 2021</span></li>
	<li><span id="Lv__COLON__EMNLP19"> [<a href="#back__Lv__COLON__EMNLP19">Lv et al., EMNLP’19</a>] <i>Xin Lv and
				Yuxian Gu and Xu Han and Lei Hou and Juanzi Li and Zhiyuan Liu</i>, Adapting Meta Knowledge Graph
			Information for Multi-Hop Reasoning over Few-Shot Relations, EMNLP, 2019</span></li>
	<li><span id="mhamdi__DASH__etal__DASH__2021__DASH__x"> [<a
				href="#back__mhamdi__DASH__etal__DASH__2021__DASH__x">M&#39;hamdi et al., NAACL’21</a>] <i>M&#39;hamdi,
				Meryem and Kim, Doo Soon and Dernoncourt, Franck and Bui, Trung and Ren, Xiang and May, Jonathan</i>,
			X-METRA-ADA: Cross-lingual Meta-Transfer learning Adaptation to Natural Language Understanding and Question
			Answering, NAACL, 2021</span></li>
	<li><span id="Madotto__COLON__ACL19"> [<a href="#back__Madotto__COLON__ACL19">Madotto et al., ACL’19</a>] <i>Andrea
				Madotto and Zhaojiang Lin and Chien-Sheng Wu and Pascale Fung</i>, Personalizing Dialogue Agents via
			Meta-Learning, ACL, 2019</span></li>
	<li><span id="Mazzawi__COLON__INTERSPEECH19"> [<a href="#back__Mazzawi__COLON__INTERSPEECH19">Mazzawi et al.,
				INTERSPEECH’19</a>] <i>Hanna Mazzawi and Xavi Gonzalvo and Aleks Kracun and Prashant Sridhar and
				Niranjan Subrahmanya and Ignacio Lopez Moreno and Hyun Jin Park and Patrick Violette</i>, Improving
			Keyword Spotting and Language Identification via Neural Architecture Search at Scale, INTERSPEECH,
			2019</span></li>
	<li><span id="Mi__COLON__IJCAI19"> [<a href="#back__Mi__COLON__IJCAI19">Mi et al., IJCAI’19</a>] <i>Fei Mi and
				Minlie Huang and Jiyong Zhang and Boi Faltings</i>, Meta-Learning for Low-resource Natural Language
			Generation in Task-oriented Dialogue Systems, IJCAI, 2019</span></li>
	<li><span id="murty__DASH__etal__DASH__2021__DASH__dreca"> [<a
				href="#back__murty__DASH__etal__DASH__2021__DASH__dreca">Murty et al., NAACL’21</a>] <i>Murty, Shikhar
				and Hashimoto, Tatsunori B. and Manning, Christopher</i>, DReCa: A General Task Augmentation Strategy
			for Few-Shot Natural Language Inference, NAACL, 2021</span></li>
	<li><span id="nooralahzadeh__DASH__etal__DASH__2020__DASH__zero"> [<a
				href="#back__nooralahzadeh__DASH__etal__DASH__2020__DASH__zero">Nooralahzadeh et al., EMNLP’20</a>]
			<i>Nooralahzadeh, Farhad and Bekoulis, Giannis and Bjerva, Johannes and Augenstein, Isabelle</i>, Zero-Shot
			Cross-Lingual Transfer with Meta Learning, EMNLP, 2020</span></li>
	<li><span id="Obamuyide__COLON__ACL19"> [<a href="#back__Obamuyide__COLON__ACL19">Obamuyide and Vlachos, ACL’19</a>]
			<i>Abiola Obamuyide and Andreas Vlachos</i>, Model-Agnostic Meta-Learning for Relation Classification with
			Limited Supervision, ACL, 2019</span></li>
	<li><span id="oguz2021few"> [<a href="#back__oguz2021few">Oguz and Vu, EACL’21</a>] <i>Oguz, Cennet and Vu, Ngoc
				Thang</i>, Few-shot Learning for Slot Tagging with Attentive Relational Network, EACL, 2021</span></li>
	<li><span id="unsupervisedMT__DASH__acl21"> [<a href="#back__unsupervisedMT__DASH__acl21">Park et al., ACL’21</a>]
			<i>Cheonbok Park and Yunwon Tae and Taehee Kim and Soyoung Yang and Mohammad Azam Khan and Eunjeong Park and
				Jaegul Choo</i>, Unsupervised Neural Machine Translation for Low-Resource Domains via Meta-Learning,
			ACL, 2021</span></li>
	<li><span id="pasunuru2019continual"> [<a href="#back__pasunuru2019continual">Pasunuru and Bansal, ACL’19</a>]
			<i>Pasunuru, Ramakanth and Bansal, Mohit</i>, Continual and Multi-Task Architecture Search, ACL, 2019</span>
	</li>
	<li><span id="pasunuru2020fenas"> [<a href="#back__pasunuru2020fenas">Pasunuru and Bansal, EMNLP’20</a>]
			<i>Pasunuru, Ramakanth and Bansal, Mohit</i>, FENAS: Flexible and Expressive Neural Architecture Search,
			EMNLP, 2020</span></li>
	<li><span id="pham2020meta"> [<a href="#back__pham2020meta">Pham et al., ICLR’21</a>] <i>Pham, Hieu and Wang, Xinyi
				and Yang, Yiming and Neubig, Graham</i>, Meta Back-Translation, ICLR, 2021</span></li>
	<li><span id="ST__DASH__dialogue__DASH__AAAI21"> [<a href="#back__ST__DASH__dialogue__DASH__AAAI21">Qian et al.,
				AAAI’21</a>] <i>Kun Qian and Wei Wei and Zhou Yu</i>, A Student-Teacher Architecture for Dialog Domain
			Adaptation under the Meta-Learning Setting, AAAI, 2021</span></li>
	<li><span id="Qian__COLON__ACL19"> [<a href="#back__Qian__COLON__ACL19">Qian et al., ACL’19</a>] <i>Kun Qian and
				Zhou Yu</i>, Domain Adaptive Dialog Generation via Meta Learning, ACL, 2019</span></li>
	<li><span id="ren2020two"> [<a href="#back__ren2020two">Ren et al., COLING’20</a>] <i>Ren, Haopeng and Cai, Yi and
				Chen, Xiaofeng and Wang, Guohua and Li, Qing</i>, A Two-phase Prototypical Network Model for Incremental
			Few-shot Relation Classification, COLING, 2020</span></li>
	<li><span id="Serra__COLON__NeurIPS19"> [<a href="#back__Serra__COLON__NeurIPS19">Serrà et al., NeurIPS’19</a>]
			<i>Joan Serrà and Santiago Pascual and Carlos Segura</i>, Blow:a single-scale hyperconditioned flow for
			non-parallel raw-audio voice conversion, NeurIPS, 2019</span></li>
	<li><span id="sheng2020adaptive"> [<a href="#back__sheng2020adaptive">Sheng et al., EMNLP’20</a>] <i>Sheng, Jiawei
				and Guo, Shu and Chen, Zhenyu and Yue, Juwei and Wang, Lihong and Liu, Tingwen and Xu, Hongbo</i>,
			Adaptive Attentional Network for Few-Shot Knowledge Graph Completion, EMNLP, 2020</span></li>
	<li><span id="Shimada__COLON__arXiv19"> [<a href="#back__Shimada__COLON__arXiv19">Shimada et al., ICASSP’20</a>]
			<i>Kazuki Shimada and Yuichiro Koyama and Akira Inoue</i>, Metric Learning with Background Noise Class for
			Few-shot Detection of Rare Sound Events, ICASSP, 2020</span></li>
	<li><span id="Sun__COLON__EMNLP18"> [<a href="#back__Sun__COLON__EMNLP18">Sun et al., EMNLP’18</a>] <i>Jingyuan Sun
				and Shaonan Wang and Chengqing Zong</i>, Memory, Show the Way:Memory Based Few Shot Word Representation
			Learning, EMNLP, 2018</span></li>
	<li><span id="Sun__COLON__EMNLP19"> [<a href="#back__Sun__COLON__EMNLP19">Sun et al., EMNLP’19</a>] <i>Shengli Sun
				and Qingfeng Sun and Kevin Zhou and Tengchao Lv</i>, Hierarchical Attention Prototypical Networks for
			Few-Shot Text Classification, EMNLP, 2019</span></li>
	<li><span id="Suris__COLON__arXiv19"> [<a href="#back__Suris__COLON__arXiv19">Surís et al., arXiv’19</a>] <i>Dídac
				Surís and Dave Epstein and Heng Ji and Shih-Fu Chang and Carl Vondrick</i>, Learning to Learn Words from
			Narrated Video, arXiv, 2019</span></li>
	<li><span id="Tan__COLON__EMNLP19"> [<a href="#back__Tan__COLON__EMNLP19">Tan et al., EMNLP’19</a>] <i>Ming Tan and
				Yang Yu and Haoyu Wang and Dakuo Wang and Saloni Potdar and Shiyu Chang and Mo Yu</i>, Out-of-Domain
			Detection for Low-Resource Text Classification Tasks, EMNLP, 2019</span></li>
	<li><span id="tarunesh2021meta"> [<a href="#back__tarunesh2021meta">Tarunesh et al., EACL’21</a>] <i>Tarunesh, Ishan
				and Khyalia, Sushil and Kumar, Vishwajeet and Ramakrishnan, Ganesh and Jyothi, Preethi</i>,
			Meta-Learning for Effective Multi-task and Multilingual Modelling, EACL, 2021</span></li>
	<li><span id="wang2020hat"> [<a href="#back__wang2020hat">Wang et al., ACL’20a</a>] <i>Wang, Hanrui and Wu, Zhanghao
				and Liu, Zhijian and Cai, Han and Zhu, Ligeng and Gan, Chuang and Han, Song</i>, HAT: Hardware-Aware
			Transformers for Efficient Natural Language Processing, ACL, 2020</span></li>
	<li><span id="wang2020balancing"> [<a href="#back__wang2020balancing">Wang et al., ACL’20b</a>] <i>Wang, Xinyi and
				Tsvetkov, Yulia and Neubig, Graham</i>, Balancing Training for Multilingual Neural Machine Translation,
			ACL, 2020</span></li>
	<li><span id="wang2019tackling"> [<a href="#back__wang2019tackling">Wang et al., EMNLP-IJCNLP’19</a>] <i>Wang, Zihao
				and Lai, Kwunping and Li, Piji and Bing, Lidong and Lam, Wai</i>, Tackling Long-Tailed Relations and
			Uncommon Entities in Knowledge Graph Completion, EMNLP-IJCNLP, 2019</span></li>
	<li><span id="wang__DASH__etal__DASH__2021__DASH__meta"> [<a
				href="#back__wang__DASH__etal__DASH__2021__DASH__meta">Wang et al., NAACL’21</a>] <i>Wang, Bailin and
				Lapata, Mirella and Titov, Ivan</i>, Meta-Learning for Domain Generalization in Semantic Parsing, NAACL,
			2021 <a href="https://aclanthology.org/2021.naacl-main.33.pdf">:link:</a></span></li>
	<li><span id="Winata__COLON__ACL2020"> [<a href="#back__Winata__COLON__ACL2020">Winata et al., ACL’20</a>] <i>Genta
				Indra Winata and Samuel Cahyawijaya and Zhaojiang Lin and Zihan Liu and Peng Xu and Pascale Fung</i>,
			Meta-Transfer Learning for Code-Switched Speech Recognition, ACL, 2020</span></li>
	<li><span id="Winata__COLON__INTERSPEECH2020"> [<a href="#back__Winata__COLON__INTERSPEECH2020">Winata et al.,
				INTERSPEECH’20</a>] <i>Genta Indra Winata and Samuel Cahyawijaya and Zihan Liu and Zhaojiang Lin and
				Andrea Madotto and Peng Xu and Pascale Fung</i>, Learning Fast Adaptation on Cross-Accented Speech
			Recognition, INTERSPEECH, 2020</span></li>
	<li><span id="Wu__COLON__AAAI20"> [<a href="#back__Wu__COLON__AAAI20">Wu et al., AAAI’20</a>] <i>Qianhui Wu and
				Zijia Lin and Guoxin Wang and Hui Chen and Börje F. Karlsson and Biqing Huang and Chin-Yew Lin</i>,
			Enhanced Meta-Learning for Cross-lingual Named Entity Recognition with Minimal Resources, AAAI, 2020</span>
	</li>
	<li><span id="Wu__COLON__EMNLP19"> [<a href="#back__Wu__COLON__EMNLP19">Wu et al., EMNLP’19</a>] <i>Jiawei Wu and
				Wenhan Xiong and William Yang Wang</i>, Learning to Learn and Predict: A Meta-Learning Approach for
			Multi-Label Classification, EMNLP, 2019</span></li>
	<li><span id="SP__DASH__ICASSP21"> [<a href="#back__SP__DASH__ICASSP21">Wu et al., ICASSP’21</a>] <i>Wu, Yuan-Kuei
				and Huang, Kuan-Po and Tsao, Yu and Lee, Hung-yi</i>, One Shot Learning for Speech Separation, ICASSP,
			2021</span></li>
	<li><span id="xia__DASH__etal__DASH__2021__DASH__metaxl"> [<a
				href="#back__xia__DASH__etal__DASH__2021__DASH__metaxl">Xia et al., NAACL’21</a>] <i>Xia, Mengzhou and
				Zheng, Guoqing and Mukherjee, Subhabrata and Shokouhi, Milad and Neubig, Graham and Awadallah, Ahmed
				Hassan</i>, MetaXL: Meta Representation Transformation for Low-resource Cross-lingual Learning, NAACL,
			2021</span></li>
	<li><span id="ASR__DASH__sample__DASH__AAAI21"> [<a href="#back__ASR__DASH__sample__DASH__AAAI21">Xiao et al.,
				AAAI’21</a>] <i>Yubei Xiao and Ke Gong and Pan Zhou and Guolin Zheng and Xiaodan Liang and Liang
				Lin</i>, Adversarial Meta Sampling for Multilingual Low-Resource Speech Recognition, AAAI, 2021</span>
	</li>
	<li><span id="Xiong__COLON__EMNLP18"> [<a href="#back__Xiong__COLON__EMNLP18">Xiong et al., EMNLP’18a</a>] <i>Wenhan
				Xiong and Mo Yu and Shiyu Chang and Xiaoxiao Guo and William Yang Wang</i>, One-Shot Relational Learning
			for Knowledge Graphs, EMNLP, 2018</span></li>
	<li><span id="xiong2018one"> [<a href="#back__xiong2018one">Xiong et al., EMNLP’18b</a>] <i>Xiong, Wenhan and Yu, Mo
				and Chang, Shiyu and Guo, Xiaoxiao and Wang, William Yang</i>, One-Shot Relational Learning for
			Knowledge Graphs, EMNLP, 2018</span></li>
	<li><span id="learningToOptimize__COLON__metaNLP21"> [<a href="#back__learningToOptimize__COLON__metaNLP21">Xu et
				al., MetaNLP’21a</a>] <i>Weijia Xu and Batool Haider and Jason Krone and Saab Mansour</i>, Soft Layer
			Selection with Meta-Learning for Zero-Shot Cross-Lingual Transfer, MetaNLP, 2021</span></li>
	<li><span id="learningToLearn__COLON__metaNLP21"> [<a href="#back__learningToLearn__COLON__metaNLP21">Xu et al.,
				MetaNLP’21b</a>] <i>Guangyue Xu and Parisa Kordjamshidi and Joyce Chai</i>, Zero-Shot Compositional
			Concept Learning, MetaNLP, 2021</span></li>
	<li><span id="yan__DASH__etal__DASH__2020__DASH__multi__DASH__source"> [<a
				href="#back__yan__DASH__etal__DASH__2020__DASH__multi__DASH__source">Yan et al., ACL’20</a>] <i>Yan,
				Ming and Zhang, Hao and Jin, Di and Zhou, Joey Tianyi</i>, Multi-source Meta Transfer for Low Resource
			Multiple-Choice Question Answering, ACL, 2020</span></li>
	<li><span id="Ye__COLON__ACL19"> [<a href="#back__Ye__COLON__ACL19">Ye and Ling, ACL’19</a>] <i>Zhi-Xiu Ye and
				Zhen-Hua Ling</i>, Multi-Level Matching and Aggregation Network for Few-Shot Relation Classification,
			ACL, 2019</span></li>
	<li><span id="yang2020frustratingly"> [<a href="#back__yang2020frustratingly">Yi and Katiyar, EMNLP’20</a>] <i>Yang,
				Yi and Katiyar, Arzoo</i>, Frustratingly Simple Few-Shot Named Entity Recognition with Structured
			Nearest Neighbor Learning, EMNLP, 2020</span></li>
	<li><span id="Yu__COLON__ACL18"> [<a href="#back__Yu__COLON__ACL18">Yu et al., ACL’18</a>] <i>Mo Yu and Xiaoxiao Guo
				and Jinfeng Yi and Shiyu Chang and Saloni Potdar and Yu Cheng and Gerald Tesauro and Haoyu Wang and
				Bowen Zhou</i>, Diverse Few-Shot Text Classification with Multiple Metrics, ACL, 2018</span></li>
	<li><span id="zhang2020few"> [<a href="#back__zhang2020few">Zhang et al., AAAI’20</a>] <i>Zhang, Chuxu and Yao,
				Huaxiu and Huang, Chao and Jiang, Meng and Li, Zhenhui and Chawla, Nitesh V</i>, Few-shot knowledge
			graph completion, AAAI, 2020</span></li>
	<li><span id="label__DASH__correction__DASH__aaai21"> [<a href="#back__label__DASH__correction__DASH__aaai21">Zheng
				et al., AAAI’21</a>] <i>Guoqing Zheng and Ahmed H. Awadallah and Susan Dumais</i>, Meta Label Correction
			for Noisy Label Learning, AAAI, 2021</span></li>
	<li><span id="MetaKD__DASH__arXiv21"> [<a href="#back__MetaKD__DASH__arXiv21">Zhou et al., arXiv’21</a>]
			<i>Wangchunshu Zhou and Canwen Xu and Julian McAuley</i>, Meta Learning for Knowledge Distillation, arXiv,
			2021</span></li>
	<li><span id="van__DASH__der__DASH__heijden__DASH__etal__DASH__2021__DASH__multilingual"> [<a
				href="#back__van__DASH__der__DASH__heijden__DASH__etal__DASH__2021__DASH__multilingual">van der Heijden
				et al., EACL’21</a>] <i>van der Heijden, Niels and Yannakoudakis, Helen and Mishra, Pushkar and Shutova,
				Ekaterina</i>, Multilingual and cross-lingual document classification: A meta-learning approach, EACL,
			2021 <a href="https://aclanthology.org/2021.eacl-main.168.pdf">:link:</a></span></li>
</ul>