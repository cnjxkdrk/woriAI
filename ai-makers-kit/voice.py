#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function

import MicrophoneStream as MS
import ex1_kwstest as kws
import ex2_getVoice2Text as gv
import ex4_getText2VoiceStream as tts
import ex6_queryVoice as dss
import time
import random

KWSID = ['또리']

return_msg = ['어서와 오늘 하루 고생 많았어어', '성연 공주우 납시오오', '잘 다녀왔어어 기다리고 있었어어']
shoes_yes_msg = ['성연이 신발 착륙 완료오오', '1단계애 성고옹', '오늘도 신발정리 완료오 잘했어']
shoes_no1_msg = ['성연아 신발 정리했니', '성연이 신발 제자리에 두었을까아']
shoes_no2_msg = ['언능하면 포인트 챙겨주지롱', '신발이는 스스로 집을 못 찾아가니까 우리가 챙겨주자', '엄마 아빠가 알면 잔소리하실지도 몰라'
			, '신발들 짝을 찾아주자', '신발을 제자리에 두는건 어때', '신발들 자리를 찾아주자']
shoes_no3_msg = ['응 뭐라구', '엇 못알아 들었어 다시 말해줄래', '잘 못들었어 다시말해주라', '다시 한 번 더 말해줄 수 있어'
			, '음 잘 안들렸어 성연이가 뭐라구 했을까']
wash_yes_msg = ['오오오 손 씻었네에 깔끔쟁이이', '캬 코로나로부터 우리 가족을 지켰네 멋져', '뽀송뽀송해졌네'
			, '수건으로 마무리해주기', '세균들 안녕', '오늘도 손 씻기 완료 내일도 잘 해줄꺼지']
wash_no1_msg = ['성연아 손 씻었어', '뽀득뽀득 했어어']
wash_no2_msg = ['코로나 바이러스 무서워 손을 안 씻으면 엄마랑 아빠가 위험할지도 몰라', '아이야 그러다 감기걸리면 엄청 아프다'
			, '비누가 아이 보고싶대 비누 만나러가자', '으아악 세균맨이다아']
wash_no3_msg = ['오잉 뭐라구', '잘 못들었어 다시 말해주라아', '음 잘 안들렸어어 성연이가아 뭐라구우 했을까아']
bag_yes_msg = ['정리정돈 기가막혀 아주', '이야 아빠가 정리정돈하는 법 아이한테 배워야겠는걸', '엄마 일 덜어주기 성공'
			, '가방이가 집에애 잘 데려다줘서어 고맙대애']
bag_no1_msg = ['성연아 가방 제대로 놨어', '가방이가아 집에애 안들어왔어어', '가방이 집에애 잘 데려다 줬어어']
bag_no2_msg = ['나중에 어딨는지 까먹는다아', '엄마가 힘들어할지도 몰라 유유', '헉 가방이가 제자리로 가고싶대'
			, '우리 가방이 집을 찾아주자아', '가방이 언제 집에 와아']
bag_no3_msg = ['잘 못들었어 미안', '잘 못들었어 다시 말해주라아', '음 잘 안들렸어어 성연이가 뭐라구우 했을까아']
off_msg = ['오늘도 칭찬 점수 많이 받았네 칭찬해', '오늘도 나랑 대화해줘서 고마워', '내말 들어줘서 고마워 성연이는 좋은 친구야'
			, '오늘처럼하면 부모님께서 성연이가 좋아하는 선물을 주실거야']

return_num = len(return_msg)
shoes_yes_num = len(shoes_yes_msg)
shoes_no1_num = len(shoes_no1_msg)
shoes_no2_num = len(shoes_no2_msg)
shoes_no3_num = len(shoes_no3_msg)
wash_yes_num = len(wash_yes_msg)
wash_no1_num = len(wash_no1_msg)
wash_no2_num = len(wash_no2_msg)
wash_no3_num = len(wash_no3_msg)
bag_yes_num = len(bag_yes_msg)
bag_no1_num = len(bag_no1_msg)
bag_no2_num = len(bag_no2_msg)
bag_no3_num = len(bag_no3_msg)
off_num = len(off_msg)

is_complete = 0
points = 0


def my_tts(text):
	tts_file = "response.wav"
	tts.getText2VoiceStream(text, tts_file)
	MS.play_file(tts_file)
	print("또리 : " + text + "\n\n\n")



def main():

	# Scene #0. 호출어 테스트
	print('================================')
	print('호출')
	print('================================')
	dss_answer = dss.queryByVoice()
	if dss_answer in KWSID:
		my_tts("안녕하세요 또리입니다.\n\n")

	a = input()


	# Scene #1. 집에 들어올 때
	print('================================')
	print('집에 들어오는 상황 시작')
	print('================================')
	
	while 1:
		dss_answer = dss.queryByVoice()	# 아이) 나왔어, 다녀왔습니다, 집이다
		if dss_answer == '':
			print('질의한 내용이 없습니다.\n\n\n')
			my_tts("다시 말씀해주세요")
		else:
			MS.play_file("result_mesg.wav") # 지니) 어서와, 오늘 하루 고생 많았어
			break

		# if dss_answer == '1':
		# 	my_tts(return_msg[random.randrange(0, return_num)])
		# else:
		# 	print('질의한 내용이 없습니다.\n\n\n')
		# 	my_tts("다시 말씀해주세요")
	
	# sleep(10)
	a = input()


	# Scene #2. 신발 정리
	print('================================')
	print('신발 정리')
	print('================================')

	# is_complete = get_shoes_flag()
	while 1:
		# 정리 O
		if is_complete == 1:
			my_tts(shoes_yes_msg[random.randrange(0, shoes_yes_num)])
			break
		# 정리 X
		else:
			my_tts(shoes_no1_msg[random.randrange(0, shoes_no1_num)])
			dss_answer = dss.queryByVoice()	# 아이 음성 인식
			if dss_answer == '1':	# 응
				is_complete = 1
			elif dss_answer == '2':	# 아니
				my_tts(shoes_no2_msg[random.randrange(0, shoes_no2_num)])
				# is_complete = get_shoes_flag()
			else:					# 몰라
				my_tts(shoes_no3_msg[random.randrange(0, shoes_no3_num)])


	is_complete = 0
	# sleep(10)
	a = input()


	# Scene #3. 손 씻기
	print('================================')
	print('손 씻기')
	print('================================')
	# is_complete = get_wash_flag()
	while 1:
		# 정리 O
		if is_complete == 1:
			my_tts(wash_yes_msg[random.randrange(0, wash_yes_num)])
			break
		# 정리 X
		else:
			my_tts(wash_no1_msg[random.randrange(0, wash_no1_num)])
			dss_answer = dss.queryByVoice()	# 아이 음성 인식
			if dss_answer == '1':	# 응
				is_complete = 1
			elif dss_answer == '2':	# 아니
				my_tts(wash_no2_msg[random.randrange(0, wash_no2_num)])
				# is_complete = get_wash_flag()
			else:					# 몰라
				my_tts(wash_no3_msg[random.randrange(0, wash_no3_num)])


	is_complete = 0
	# sleep(10)
	a = input()


	# Scene #4. 물품 정리
	print('================================')
	print('물품 정리')
	print('================================')
	# is_complete = get_bag_flag()
	while 1:
		# 정리 O
		if is_complete == 1:
			my_tts(bag_yes_msg[random.randrange(0, bag_yes_num)])
			break
		# 정리 X
		else:
			my_tts(bag_no1_msg[random.randrange(0, bag_no1_num)])
			dss_answer = dss.queryByVoice()	# 아이 음성 인식
			if dss_answer == '1':	# 응
				is_complete = 1
			elif dss_answer == '2':	# 아니
				my_tts(bag_no2_msg[random.randrange(0, bag_no2_num)])
				# is_complete = get_bag_flag()
			else:					# 몰라
				my_tts(bag_no3_msg[random.randrange(0, bag_no3_num)])


	is_complete = 0
	# sleep(10)
	a = input()

	
	# Scene #5. 종료

	my_tts(off_msg[random.randrange(0, off_num)])
	print('================================')
	print('점수: ' + points)
	print('================================')

"""
	KWSID = ['기가지니', '지니야', '친구야', '자기야']
	while 1:
		recog=kws.test(KWSID[0])
		if recog == 200:
			print('KWS Dectected ...\n')
			dss_answer = dss.queryByVoice()
			if dss_answer == '':
				print('질의한 내용이 없습니다.\n\n\n')
			else:
				MS.play_file("result_mesg.wav")			
			time.sleep(2)
		else:
			print('KWS Not Dectected ...')
"""		

if __name__ == '__main__':
    main()
