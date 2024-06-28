import { shallowMount } from '@vue/test-utils';
import CameraIcon from './CameraIcon.vue';





describe('<CameraIcon/>', () => {
	const wrapper = shallowMount(CameraIcon);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(CameraIcon);
		expect(wrapper2.html()).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });

